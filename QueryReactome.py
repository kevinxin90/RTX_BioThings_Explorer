import sys
import re

from QueryBioThingsExplorer import QueryBioThingsExplorer


class QueryReactome:
    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()
        self.SPECIES_MNEMONICS = ['BOVIN', 'ACAVI', 'VACCW', 'PLAVS', 'CHICK', 'ECOLI', 'HORSE', 'MAIZE', 'MOUSE',
                                  'PEA', 'PIG', 'RABIT', 'RAT', 'SHEEP', 'SOYBN', 'TOBAC', 'WHEAT', 'YEAST', 'HV1N5',
                                  'HV1H2', 'DANRE', 'XENLA', 'MYCTU', 'HHV8P', 'HTLV2', 'HHV1', 'HPV16', '9HIV1',
                                  'EBVB9', 'PROBE', 'HTL1C', 'I72A2', 'SV40', 'HV1B1', 'SCHPO', 'RUBV', 'MUS']

    def is_valid_uniprot_accession(self, accession_str):
        return re.match("[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}",
                        accession_str) is not None

    def query_uniprot_id_to_interacting_uniprot_ids_desc(self, uniprot_id):
        res = self.biothings_explorer.send_query_get(input_prefix='uniprot', output_prefix="uniprot",
                                                     input_value=uniprot_id)
        res_uniprot_ids = dict()
        if res:
            res = [_doc for _doc in res['data'] if _doc[
                'endpoint'] == "https://reactome.org/ContentService/interactors/static/molecule/{uniprot}/details"]
            if res:
                for res_entity_interactor in res:
                    int_uniprot_id = res_entity_interactor['output']['object']['id'][len('uniprot') + 1:]
                    if 'CHEBI:' not in int_uniprot_id:
                        if '-' in int_uniprot_id:
                            int_uniprot_id = int_uniprot_id.split('-')[0]
                        if 'secondary-id' in res_entity_interactor['output']['object']:
                            int_alias = res_entity_interactor['output']['object']['secondary-id'][
                                        len('hgnc.symbol') + 1:]
                        else:
                            int_alias = ''
                        alt_species = None
                        if ' ' in int_alias:
                            int_alias_split = int_alias.split(' ')
                            int_alias = int_alias_split[0]
                            alt_species = int_alias_split[1]
                        if alt_species is None or (alt_species not in self.SPECIES_MNEMONICS and \
                                                           not (alt_species[0] == '9')):
                            if alt_species is not None:
                                if 'DNA' in int_alias_split or \
                                                'DNA-PROBE' in int_alias_split or \
                                                'DSDNA' in int_alias_split or \
                                                'GENE' in int_alias_split or \
                                                'PROMOTE' in int_alias_split or \
                                                'PROMOTER' in int_alias_split or \
                                        any(['-SITE' in alias_element for alias_element in int_alias_split]) or \
                                        any(['BIND' in alias_element for alias_element in int_alias_split]):
                                    target_gene_symbol = int_alias_split[0]
                                    int_alias = 'BINDSGENE:' + int_alias_split[0]
                                else:
                                    print(
                                        'For query protein ' + uniprot_id + ' and interactant protein ' + int_uniprot_id + ', check for potential other species name in Reactome output: ' + alt_species,
                                        file=sys.stderr)
                                    int_alias = None
                        if int_alias is not None and int_alias != "" and self.is_valid_uniprot_accession(
                                int_uniprot_id):
                            res_uniprot_ids[int_uniprot_id] = int_alias
        return res_uniprot_ids

    def __query_uniprot_to_reactome_entity_id(self, uniprot_id):
        res = self.biothings_explorer.send_query_get(input_prefix='uniprot', output_prefix="reactome.complex",
                                                     input_value=uniprot_id)
        if res:
            ret_ids = set([_doc['output']['object']['id'].split(':')[1] for _doc in res['data']])
            return ret_ids
        else:
            return None

    def __query_uniprot_to_reactome_entity_id_desc(self, uniprot_id):
        res = self.biothings_explorer.send_query_get(input_prefix='uniprot', output_prefix="reactome.complex",
                                                     input_value=uniprot_id)
        reactome_ids_dict = dict()
        if res:
            for _doc in res['data']:
                res_id = _doc['output']['object']['id'].split(':')[1]
                if res_id.startswith('R-HSA-'):
                    reactome_ids_dict[res_id] = _doc['output']['object']['secondary-id'][len("reactome.displayname:"):]
        return reactome_ids_dict

    def __query_reactome_entity_id_to_reactome_pathway_ids_desc(self, reactome_entity_id):
        res = self.biothings_explorer.send_query_get(input_prefix='reactome.complex', output_prefix="reactome.pathway",
                                                     input_value=reactome_entity_id)
        reactome_ids_dict = dict()
        if res:
            for _doc in res['data']:
                res_id = _doc['output']['object']['id'].split(':')[1]
                if res_id.startswith('R-HSA-'):
                    reactome_ids_dict[res_id] = _doc['output']['object']['secondary-id'][len("reactome.displayname:"):]
        return reactome_ids_dict

    def query_uniprot_id_to_reactome_pathway_ids_desc(self, uniprot_id):
        reactome_entity_ids = self.__query_uniprot_to_reactome_entity_id(uniprot_id)
        res_dict = dict()
        for reactome_entity_id in reactome_entity_ids:
            if reactome_entity_id.startswith('R-HSA-'):
                pathway_ids_dict = self.__query_reactome_entity_id_to_reactome_pathway_ids_desc(reactome_entity_id)
                if len(pathway_ids_dict) > 0:
                    res_dict.update(pathway_ids_dict)
        return res_dict

    def query_reactome_pathway_id_to_uniprot_ids_desc(self, reactome_pathway_id):
        res = self.biothings_explorer.send_query_get(input_prefix='reactome.pathway', output_prefix="uniprot",
                                                     input_value=reactome_pathway_id)
        ret_dict = dict()
        if res:
            participant_ids_list = [_doc['output']['object']['secondary-id'] for _doc in res['data']]
            for participant_id in participant_ids_list:
                if 'UniProt:' in participant_id:
                    uniprot_id = participant_id.split(' ')[0].split(':')[-1]
                    if ' ' in participant_id:
                        prot_desc = participant_id.split(' ')[1]
                    else:
                        prot_desc = 'UNKNOWN'
                    if '-' in uniprot_id:
                        uniprot_id = uniprot_id.split('-')[0]
                    ret_dict[uniprot_id] = prot_desc
        return ret_dict

    def test(self):
        print(QueryReactome().query_uniprot_id_to_interacting_uniprot_ids_desc("P62991"))
        print(QueryReactome().is_valid_uniprot_accession("Q16665"))
        print(QueryReactome().is_valid_uniprot_accession("EBI"))
        print(QueryReactome().query_uniprot_id_to_interacting_uniprot_ids_desc("Q16665"))
        print(QueryReactome().query_uniprot_id_to_interacting_uniprot_ids_desc('P04150'))
        print(QueryReactome().query_uniprot_id_to_interacting_uniprot_ids_desc('Q06609'))
        print(QueryReactome().query_uniprot_id_to_interacting_uniprot_ids_desc('Q13501'))
        print(QueryReactome().query_uniprot_id_to_interacting_uniprot_ids_desc('P68871'))
        print(QueryReactome().query_uniprot_id_to_interacting_uniprot_ids_desc('O75521-2'))
        print(QueryReactome().query_reactome_pathway_id_to_uniprot_ids_desc('R-HSA-5423646'))
        # print(QueryReactome().query_uniprot_id_to_reactome_pathway_ids_desc('P68871'))
        print(QueryReactome().__query_uniprot_to_reactome_entity_id('O75521-2'))
        print(QueryReactome().__query_uniprot_to_reactome_entity_id('P68871'))
        print(QueryReactome().__query_reactome_entity_id_to_reactome_pathway_ids_desc('R-HSA-2230989'))
        print(QueryReactome().__query_uniprot_to_reactome_entity_id_desc('P68871'))


if __name__ == '__main__':
    QueryReactome().test()

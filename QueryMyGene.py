import requests
import sys

from QueryBioThingsExplorer import QueryBioThingsExplorer

class QueryMyGene:

    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()

    def convert_gene_symbol_to_uniprot_id(self, gene_symbol):
        entrez_gene_ids = self.convert_gene_symbol_to_entrez_gene_ID(gene_symbol)
        if entrez_gene_ids:
            results = set()
            for entrez_gene in entrez_gene_ids:
                mygene_results = self.biothings_explorer.send_query_get(input_prefix='ncbigene', output_prefix="uniprot", input_value=str(entrez_gene))
                if mygene_results:
                    for _result in mygene_results['data']:
                        if type(_result['output']['object']['id']) == list:
                            for _uniprot in _result['output']['object']['id']:
                                results.add(_uniprot.split(':')[-1])
                        else:
                            results.add(_result['output']['object']['id'].split(':')[-1])
            return results
        else:
            return set()

    def convert_uniprot_id_to_gene_symbol(self, uniprot_id):
        mygene_results = self.biothings_explorer.send_query_get(input_prefix='uniprot', output_prefix="ncbigene", input_value=uniprot_id)
        if mygene_results:
            gene_symbol = set([_doc['output']['object']['secondary-id'].split(':')[-1] for _doc in mygene_results['data'] if _doc['output']['object']['taxonomy'] == "9606"])
            return gene_symbol
        else:
            return set()

    def convert_uniprot_id_to_entrez_gene_ID(self, uniprot_id):
        mygene_results = self.biothings_explorer.send_query_get(input_prefix='uniprot', output_prefix="ncbigene", input_value=uniprot_id)
        if mygene_results:
            entrez_ids = set([int(_doc['output']['object']['id'].split(':')[-1]) for _doc in mygene_results['data'] if _doc['output']['object']['taxonomy'] == "9606"])
            return entrez_ids
        else:
            return set()

    def convert_gene_symbol_to_entrez_gene_ID(self, gene_symbol):
        mygene_results = self.biothings_explorer.send_query_get(input_prefix='hgnc.symbol', output_prefix="ncbigene", input_value=gene_symbol)
        if mygene_results:
            entrez_ids = set([int(_doc['output']['object']['id'].split(':')[-1]) for _doc in mygene_results['data'] if 'taxonomy' in _doc['output']['object'] and _doc['output']['object']['taxonomy'] == "9606"])
            return entrez_ids
        else:
            return set()

    def convert_entrez_gene_ID_to_mirbase_ID(self, entrez_gene_id):
        mygene_results = self.biothings_explorer.send_query_get(input_prefix="ncbigene", output_prefix="mirbase", input_value=str(entrez_gene_id))
        if mygene_results:
            mirbase_id = set([_doc['output']['object']['id'].split(':')[-1] for _doc in mygene_results['data']])
            return mirbase_id
        else:
            return set()

    def get_gene_ontology_ids_bp_for_uniprot_id(self, uniprot_id):
        entrez_ids = self.convert_uniprot_id_to_entrez_gene_ID(uniprot_id)
        if entrez_ids:
            res = dict()
            for entrez_id in entrez_ids:
                mygene_results = self.get_gene_ontology_ids_bp_for_entrez_gene_id(str(entrez_id))
                if mygene_results:
                    res.update(mygene_results)
            return res
        else:
            return dict()


    def get_cui(self, gene_id):
        if gene_id.startswith('NCBIGene'):
            gene_id = gene_id.split(':')[1]
            entrez_ids = self.biothings_explorer.send_query_get(input_prefix="ncbigene", output_prefix="umls.gene", input_value=gene_id)
            if entrez_ids:
                cuis = [_doc['output']['object']['id'].split(':')[-1] for _doc in entrez_ids['data']]
                return cuis
            else:
                return None
        elif gene_id.startswith('UniProt'):
            uniprot_id = gene_id.split(':')[1]
            entrez_ids = self.convert_uniprot_id_to_entrez_gene_ID(uniprot_id)
            if entrez_ids:
                cuis = []
                for _entrez_id in entrez_ids:
                    umls = self.biothings_explorer.send_query_get(input_prefix="ncbigene", output_prefix="umls.gene", input_value=str(_entrez_id))
                    cuis += [_doc['output']['object']['id'].split(':')[-1] for _doc in umls['data']]
                return cuis
            else:
                return None

    def get_gene_ontology_ids_bp_for_entrez_gene_id(self, entrez_gene_id):
        mygene_results = self.biothings_explorer.send_query_get(input_prefix="ncbigene", output_prefix="go", input_value=str(entrez_gene_id))
        if mygene_results:
            gene_ontology_id = {('GO:' + _doc['output']['object']['id'].split(':')[-1]): _doc['output']['object']['label'].split(':')[-1] for _doc in mygene_results['data']}
            return gene_ontology_id
        else:
            return {}

    def uniprot_id_is_human(self, uniprot_id_str):
        mygene_results = self.biothings_explorer.send_query_get(input_prefix='uniprot', output_prefix="ncbigene", input_value=uniprot_id_str)
        if mygene_results:
            taxonomy = [_doc['output']['object']['taxonomy'] for _doc in mygene_results['data']]
            if '9606' in taxonomy:
                return True
            else:
                return False
        else:
            return False

if __name__ == '__main__':
    mg = QueryMyGene()
    print(mg.convert_uniprot_id_to_gene_symbol('Q8NBZ7'))
    print(mg.get_gene_ontology_ids_bp_for_uniprot_id('Q05925'))
    print(mg.uniprot_id_is_human("P02794"))
    print(mg.uniprot_id_is_human("P10592"))
    print(mg.convert_entrez_gene_ID_to_mirbase_ID(407053))
    print(mg.get_gene_ontology_ids_bp_for_entrez_gene_id(406991))
    print(mg.convert_uniprot_id_to_gene_symbol('Q05925'))
    print(mg.convert_gene_symbol_to_uniprot_id('A2M'))
    print(mg.convert_gene_symbol_to_uniprot_id('A1BG'))
    print(mg.convert_gene_symbol_to_entrez_gene_ID('MIR96'))
    print(mg.convert_gene_symbol_to_uniprot_id("HMOX1"))
    print(mg.convert_gene_symbol_to_uniprot_id('RAD54B'))
    print(mg.convert_gene_symbol_to_uniprot_id('NS2'))
    print(mg.convert_uniprot_id_to_gene_symbol("P09601"))
    print(mg.convert_uniprot_id_to_entrez_gene_ID("P09601"))
    print(mg.convert_uniprot_id_to_entrez_gene_ID("XYZZY")) 

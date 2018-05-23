import requests
import sys

from QueryBioThingsExplorer import QueryBioThingsExplorer

class QueryPharos:

    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()

    def query_drug_id_by_name(self, drug_name):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='drugname', output_prefix="pharos.ligand", input_value=drug_name)
        if pharos_results:
            drug_id = None
            for _result in pharos_results['data']:
                if _result['output']['object']['secondary-id'] == ('drugname:' + drug_name):
                    drug_id = _result['output']['object']['id'].split(':')[-1]
            if drug_id:
                return int(drug_id)
            else:
                return None

        else:
            return None

    def query_drug_name(self, ligand_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.ligand', output_prefix="drugname", input_value=ligand_id)
        if pharos_results:
            drug_name = pharos_results['data'][0]['output']['object']['id'].split(':')[-1]
            return drug_name
        else:
            return None

    def query_disease_name(self, disease_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.disease', output_prefix="diseasename", input_value=disease_id)
        if pharos_results:
            disease_name = pharos_results['data'][0]['output']['object']['id'].split(':')[-1]
            return disease_name
        else:
            return None

    def query_target_uniprot_accession(self, target_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.target', output_prefix="uniprot", input_value=target_id)
        if pharos_results:
            uniprot = pharos_results['data'][0]['output']['object']['id'].split(':')[-1]
            return uniprot
        else:
            return None

    def query_target_name(self, target_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.target', output_prefix="gene-approved-name", input_value=target_id)
        if pharos_results:
            gene_symbols = pharos_results['data'][0]['output']['object']['id'][len('gene-approved-name')+1:]
            return gene_symbols
        else:
            return None

    def query_drug_to_targets(self, drug_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.ligand', output_prefix="pharos.target", input_value=drug_id)
        if pharos_results:
            ret_ids = []
            for _doc in pharos_results['data']:
                ret_ids.append({'id': _doc['output']['object']['id'].split(':')[-1], 
                                'name': _doc['output']['object']['secondary-id'].split(':')[-1]
                                })
            return ret_ids
        else:
            return []

    def query_target_to_drugs(self, target_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.target', output_prefix="pharos.ligand", input_value=target_id)
        if pharos_results:
            ret_ids = []
            for _doc in pharos_results['data']:
                if 'edge' in _doc['output']:
                    ret_ids.append({'id': _doc['output']['object']['id'].split(':')[-1], 
                                    'label': _doc['output']['object']['secondary-id'].split(':')[-1],
                                    'action': _doc['output']['edge']['label']})
            return ret_ids
        else:
            return []

    def query_target_to_diseases(self, target_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.target', output_prefix="pharos.disease", input_value=target_id)
        ret_ids = []
        for _doc in pharos_results['data']:
            ret_ids.append({'id': _doc['output']['object']['id'].split(':')[-1], 
                            'label': _doc['output']['object']['secondary-id'].split(':')[-1]})
        return ret_ids

    def query_drug_name_to_targets(self, drug_name):
        drug_ids = self.query_drug_id_by_name(drug_name)
        if drug_ids:
            ret_ids = []
            target_id_list = []
            res = self.biothings_explorer.send_query_get(input_prefix='pharos.ligand', output_prefix="pharos.target", input_value=str(drug_ids))
            for _doc in res['data']:
                if _doc['output']['object']['id'] not in target_id_list:
                    target_id_list.append(_doc['output']['object']['id'])
                    ret_ids.append( { 'id': _doc['output']['object']['id'].split(':')[-1], 'name': _doc['output']['object']['secondary-id'].split(':')[-1]})
            return ret_ids
        else:
            return None

    def query_disease_id_by_name(self, disease_name):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='diseasename', output_prefix="pharos.disease", input_value=disease_name)
        if pharos_results:
            disease_id = None
            for _result in pharos_results['data']:
                if _result['output']['object']['secondary-id'] == ('diseasename:' + disease_name):
                    disease_id = _result['output']['object']['id'].split(':')[-1]
            if disease_id:
                return int(disease_id)
            else:
                return None

        else:
            return None

if __name__ == '__main__':
    #print(QueryPharos().query_drug_id_by_name('paclitaxel'))
    #print(QueryPharos().query_drug_to_targets("254599"))
    #print(QueryPharos().query_drug_to_targets("1"))
    #print(QueryPharos().query_drug_id_by_name('clothiapine'))
    #print(QueryPharos().query_drug_id_by_name("lovastatin"))
    #print(QueryPharos().query_drug_to_targets("1"))
    #print(QueryPharos().query_target_uniprot_accession("1"))  
    #print(QueryPharos().query_target_to_drugs("16012"))
    #print(QueryPharos().query_target_name("852"))
    print(QueryPharos().query_drug_name("1"))

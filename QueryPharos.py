import requests
import sys

from QueryBioThingsExplorer import QueryBioThingsExplorer

class QueryPharos:

    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()

    def query_drug_id_by_name(self, drug_name):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='drugname', output_prefix="pharos.ligand", input_value=drug_name)
        drug_id = set([_doc['output']['object']['id'].split(':')[-1] for _doc in pharos_results['data']])
        return drug_id

    def query_drug_name(self, ligand_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.ligand', output_prefix="drugname", input_value=ligand_id)
        drug_name = set([_doc['output']['object']['id'].split(':')[-1] for _doc in pharos_results['data']])
        return drug_name

    def query_disease_name(self, disease_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.disease', output_prefix="diseasename", input_value=disease_id)
        disease_name = set([_doc['output']['object']['id'].split(':')[-1] for _doc in pharos_results['data']])
        return disease_name

    def query_target_uniprot_accession(self, target_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.target', output_prefix="uniprot", input_value=target_id)
        uniprot = set([_doc['output']['object']['id'].split(':')[-1] for _doc in pharos_results['data']])
        return uniprot

    def query_target_name(self, target_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.target', output_prefix="hgnc.symbol", input_value=target_id)
        gene_symbols = set([_doc['output']['object']['id'].split(':')[-1] for _doc in pharos_results['data']])
        return gene_symbols

    def query_drug_to_targets(self, drug_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.ligand', output_prefix="pharos.target", input_value=drug_id)
        ret_ids = []
        for _doc in pharos_results['data']:
            ret_ids.append({'id': _doc['output']['object']['id'].split(':')[-1], 
                            'label': _doc['output']['object']['secondary-id'].split(':')[-1]})
        return ret_ids

    def query_target_to_drugs(self, target_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.target', output_prefix="pharos.ligand", input_value=target_id)
        ret_ids = []
        for _doc in pharos_results['data']:
            ret_ids.append({'id': _doc['output']['object']['id'].split(':')[-1], 
                            'label': _doc['output']['object']['secondary-id'].split(':')[-1]})
        return ret_ids

    def query_target_to_diseases(self, target_id):
        pharos_results = self.biothings_explorer.send_query_get(input_prefix='pharos.target', output_prefix="pharos.disease", input_value=target_id)
        ret_ids = []
        for _doc in pharos_results['data']:
            ret_ids.append({'id': _doc['output']['object']['id'].split(':')[-1], 
                            'label': _doc['output']['object']['secondary-id'].split(':')[-1]})
        return ret_ids

if __name__ == '__main__':
    print(QueryPharos().query_drug_id_by_name('paclitaxel'))
    print(QueryPharos().query_drug_to_targets("1"))
    print(QueryPharos().query_drug_id_by_name("lovastatin"))
    print(QueryPharos().query_drug_to_targets("1"))    

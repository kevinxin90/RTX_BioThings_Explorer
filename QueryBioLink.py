import requests
import sys

from QueryBioThingsExplorer import QueryBioThingsExplorer

class QueryBioLink:
    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()

    def get_phenotypes_for_disease_desc(self, disease_id):
        results = self.biothings_explorer.send_query_get(input_prefix='omim.disease', output_prefix='hp', input_value=disease_id)
        res_dict = {_doc['output']['object']['id'].upper(): _doc['output']['object']['secondary-id'].split(':')[-1] for _doc in results['data']}
        return res_dict

    def get_phenotypes_for_gene(self, gene_id):
        results = self.biothings_explorer.send_query_get(input_prefix='ncbigene', output_prefix='hp', input_value=gene_id)
        res_dict = {_doc['output']['object']['id'].upper(): _doc['output']['object']['secondary-id'].split(':')[-1] for _doc in results['data']}
        return res_dict

    def get_anatomies_for_gene(self, gene_id):
        results = self.biothings_explorer.send_query_get(input_prefix='ncbigene', output_prefix='uberon', input_value=gene_id)
        res_dict = {_doc['output']['object']['id'].upper(): _doc['output']['object']['label'] for _doc in results['data']}
        return res_dict

if __name__ == '__main__':
    print(QueryBioLink().get_phenotypes_for_disease_desc('605543'))
    print(QueryBioLink().get_phenotypes_for_gene('4750'))
    print(QueryBioLink().get_anatomies_for_gene('407053'))

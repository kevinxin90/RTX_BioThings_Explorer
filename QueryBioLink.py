import requests
import sys

from QueryBioThingsExplorer import QueryBioThingsExplorer

class QueryBioLink():
    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()

    def get_label_for_disease(self, disease_id):
        disease_prefix = disease_id.split(':')[0]
        disease_value = disease_id.split(':')[1]
        if disease_prefix == "MONDO":
            results = self.biothings_explorer.send_query_get(input_prefix='mondo', output_prefix='diseasename', input_value=disease_value)
        elif disease_prefix == "OMIM":
            results = self.biothings_explorer.send_query_get(input_prefix='omim.disease', output_prefix='diseasename', input_value=disease_value)
        elif disease_prefix == "DOID":
            results = self.biothings_explorer.send_query_get(input_prefix='do', output_prefix='diseasename', input_value=disease_value)
        if results:
            res = results['data'][0]['output']['object']['id'][len('diseasename')+1:]
            return res
        else:
            return None

    def get_label_for_phenotype(self, phenotype_id):
        phenotype_id = phenotype_id.split(':')[-1]
        results = self.biothings_explorer.send_query_get(input_prefix='hp', output_prefix='phenotypeName', input_value=phenotype_id)
        if results:
            res = results['data'][0]['output']['object']['id'][len('phenotypename')+1:]
            return res
        else:
            return None

    def get_diseases_for_gene_desc(self, gene_id):
        gene_id = gene_id.split(':')[-1]
        results = self.biothings_explorer.send_query_get(input_prefix='ncbigene', output_prefix='mondo', input_value=gene_id)
        if results:
            res_list = {_doc['output']['object']['id'].upper(): _doc['output']['object']['secondary-id'][len("diseasename")+1:] for _doc in results['data']}
            return res_list
        else:
            return []

    def get_genes_for_disease_desc(self, disease_id):
        disease_id = disease_id.split(':')[-1]
        results = self.biothings_explorer.send_query_get(input_prefix='omim.disease', output_prefix='hgnc', input_value=disease_id)
        if results:
            res_list = [_doc['output']['object']['id'].upper() for _doc in results['data']]
            return res_list
        else:
            return []

    def get_phenotypes_for_disease_desc(self, disease_id):
        disease_id = disease_id.split(':')[-1]
        results = self.biothings_explorer.send_query_get(input_prefix='omim.disease', output_prefix='hp', input_value=disease_id)
        if results:
            res_dict = {_doc['output']['object']['id'].upper(): _doc['output']['object']['secondary-id'].split(':')[-1] for _doc in results['data']}
            return res_dict
        else:
            return {}

    def get_phenotypes_for_gene(self, gene_id):
        gene_id = gene_id.split(':')[-1]
        results = self.biothings_explorer.send_query_get(input_prefix='ncbigene', output_prefix='hp', input_value=gene_id)
        if results:
            res_dict = [_doc['output']['object']['id'].upper() for _doc in results['data']]
            return res_dict
        else:
            return []

    def get_phenotypes_for_gene_desc(self, gene_id):
        gene_id = gene_id.split(':')[-1]
        results = self.biothings_explorer.send_query_get(input_prefix='ncbigene', output_prefix='hp', input_value=gene_id)
        if results:
            res_dict = {_doc['output']['object']['id'].upper(): _doc['output']['object']['secondary-id'].split(':')[-1] for _doc in results['data']}
            return res_dict
        else:
            return {}

    def get_anatomies_for_gene(self, gene_id):
        gene_id = gene_id.split(':')[-1]
        results = self.biothings_explorer.send_query_get(input_prefix='ncbigene', output_prefix='uberon', input_value=gene_id)
        if results:
            res_dict = {_doc['output']['object']['id'].upper(): _doc['output']['object']['label'] for _doc in results['data']}
            return res_dict
        else:
            return None

    def get_genes_for_anatomy(self, anatomy_id):
        anatomy_id = anatomy_id.split(':')[-1]
        results = self.biothings_explorer.send_query_get(input_prefix='uberon', output_prefix='hgnc', input_value=anatomy_id)
        if results:
            res_dict = [_doc['output']['object']['id'].upper() for _doc in results['data']]
            return res_dict
        else:
            return None

    def get_anatomies_for_phenotype(self, phenotype_id):
        phenotype_id = phenotype_id.split(':')[-1]
        results = self.biothings_explorer.send_query_get(input_prefix='hp', output_prefix='uberon', input_value=phenotype_id)
        if results:
            res_dict = {_doc['output']['object']['id'].upper(): _doc['output']['object']['secondary-id'].split(':')[-1] for _doc in results['data']}
            return res_dict
        else:
            return None

if __name__ == '__main__':
    print(QueryBioLink().get_phenotypes_for_disease_desc('OMIM:605543'))
    print(QueryBioLink().get_genes_for_disease_desc('OMIM:XXXXXX'))
    print(QueryBioLink().get_genes_for_disease_desc('OMIM:605543'))
    print(QueryBioLink().get_phenotypes_for_gene_desc('NCBIGene:1080'))  # test for issue #22
    print(QueryBioLink().get_diseases_for_gene_desc('NCBIGene:407053'))
    print(QueryBioLink().get_diseases_for_gene_desc('NCBIGene:100048912'))
    print(QueryBioLink().get_phenotypes_for_gene_desc('NCBIGene:4750'))
    print(QueryBioLink().get_phenotypes_for_gene('NCBIGene:4750'))
    print(QueryBioLink().get_diseases_for_gene_desc('NCBIGene:4750'))
    print(QueryBioLink().get_diseases_for_gene_desc('NCBIGene:1111111'))
    print(QueryBioLink().get_label_for_disease('DOID:1498'))
    print(QueryBioLink().get_label_for_disease('OMIM:605543'))
    print(QueryBioLink().get_label_for_phenotype('HP:0000003'))
    print(QueryBioLink().get_anatomies_for_gene('NCBIGene:407053'))
    print(QueryBioLink().get_genes_for_anatomy('UBERON:0000006'))
    print(QueryBioLink().get_anatomies_for_phenotype('HP:0000003'))
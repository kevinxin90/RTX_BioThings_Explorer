import requests
import sys

from QueryBioThingsExplorer import QueryBioThingsExplorer

class QueryEBIOLSExtended:

    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()

    def get_anatomy_description(self, anatomy_id):
        prefix = anatomy_id.split(':')[0]
        anatomy_value = anatomy_id.split(':')[1]
        if prefix.upper() == 'CL':
            ols_results = self.biothings_explorer.send_query_get(input_prefix='cl', output_prefix="anatomyDescription", input_value=anatomy_value)
        elif prefix.upper() == 'UBERON':
            ols_results = self.biothings_explorer.send_query_get(input_prefix='uberon', output_prefix="anatomyDescription", input_value=anatomy_value)
        else:
            ols_results = None
        if ols_results:
            return ols_results['data'][0]['output']['object']['id'][len('anatomyDescription') + 1:]
        else:
            return "None"  # See https://github.com/RTXteam/RTX/issues/140

    def get_bio_process_description(self, bio_process_id):
        bio_process_value = bio_process_id.split(':')[-1]
        ols_results = self.biothings_explorer.send_query_get(input_prefix='go', output_prefix="goDescription", input_value=bio_process_value)
        if ols_results:
            return ols_results['data'][0]['output']['object']['id'][len('goDescription') + 1:]
        else:
            return "None"  # See https://github.com/RTXteam/RTX/issues/140

    def get_phenotype_description(self, phenotype_id):
        pheontype_value = phenotype_id.split(':')[-1]
        ols_results = self.biothings_explorer.send_query_get(input_prefix='hp', output_prefix="phenotypeDescription", input_value=pheontype_value)
        if ols_results:
            return ols_results['data'][0]['output']['object']['id'][len('phenotypeDescription') + 1:]
        else:
            return "None"  # See https://github.com/RTXteam/RTX/issues/140

    def get_disease_description(self, disease_id):
        disease_value = disease_id.split(':')[-1]
        ols_results = self.biothings_explorer.send_query_get(input_prefix='do', output_prefix="diseaseDescription", input_value=disease_value)
        if ols_results:
            return ols_results['data'][0]['output']['object']['id'][len('diseaseDescription') + 1:]
        else:
            return "None"  # See https://github.com/RTXteam/RTX/issues/140

    def get_cellular_component_description(self, cc_id):
        cc_value = cc_id.split(':')[-1]
        ols_results = self.biothings_explorer.send_query_get(input_prefix='go', output_prefix="goDescription", input_value=cc_value)
        if ols_results:
            return ols_results['data'][0]['output']['object']['id'][len('goDescription') + 1:]
        else:
            return "None"  # See https://github.com/RTXteam/RTX/issues/140

    def get_molecular_function_description(self, mf_id):
        mf_value = mf_id.split(':')[-1]
        ols_results = self.biothings_explorer.send_query_get(input_prefix='go', output_prefix="goDescription", input_value=mf_value)
        if ols_results:
            return ols_results['data'][0]['output']['object']['id'][len('goDescription') + 1:]
        else:
            return "None"  # See https://github.com/RTXteam/RTX/issues/140

if __name__ == '__main__':
    # print('UBERON:0004476', QueryEBIOLSExtended().get_anatomy_description('UBERON:0004476'))
    print('UBERON:00044760', QueryEBIOLSExtended().get_anatomy_description('UBERON:00044760'))
    # print('CL:0000038', QueryEBIOLSExtended().get_anatomy_description('CL:0000038'))
    # print('CL:00000380', QueryEBIOLSExtended().get_anatomy_description('CL:00000380'))
    # print('GO:0042535', QueryEBIOLSExtended().get_bio_process_description('GO:0042535'))
    # print('GO:00425350', QueryEBIOLSExtended().get_bio_process_description('GO:00425350'))
    # print('HP:0011105', QueryEBIOLSExtended().get_phenotype_description('HP:0011105'))
    # print('HP:00111050', QueryEBIOLSExtended().get_phenotype_description('HP:00111050'))
    # print('GO:0005573', QueryEBIOLSExtended().get_cellular_component_description('GO:0005573'))
    # print('GO:00055730', QueryEBIOLSExtended().get_cellular_component_description('GO:00055730'))
    # print('GO:0004689', QueryEBIOLSExtended().get_molecular_function_description('GO:0004689'))
    # print('GO:00046890', QueryEBIOLSExtended().get_molecular_function_description('GO:00046890'))
    # print('OMIM:613573', QueryEBIOLSExtended().get_disease_description('OMIM:613573'))
    # print('OMIM:6135730', QueryEBIOLSExtended().get_disease_description('OMIM:6135730'))

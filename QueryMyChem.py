from QueryBioThingsExplorer import QueryBioThingsExplorer

class QueryMyChem:

    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()

    def get_chemical_substance_description(self, chemical_substance_id):
        chembl_id = chemical_substance_id.replace("ChEMBL:", "CHEMBL")
        chembl_results = self.biothings_explorer.send_query_get(input_prefix='chembl.compound', output_prefix="chemicalDescription", input_value=chembl_id)
        if chembl_results:
            return chembl_results['data'][0]['output']['object']['id'][len("chemicalDescription") + 1:]
        else:
            return None
    
    def get_mesh_id(self, chemical_substance_id):
        chembl_id = chemical_substance_id.replace("ChEMBL:", "CHEMBL")
        chembl_results = self.biothings_explorer.send_query_get(input_prefix='chembl.compound', output_prefix="mesh.compound", input_value=chembl_id)
        if chembl_results:
            return chembl_results['data'][0]['output']['object']['id'][len("mesh.compound") + 1:]
        else:
            return None

    def get_cui(self, chemical_substance_id):
        chembl_id = chemical_substance_id.replace("ChEMBL:", "CHEMBL")
        chembl_results = self.biothings_explorer.send_query_get(input_prefix='chembl.compound', output_prefix="umls.compound", input_value=chembl_id)
        if chembl_results:
            return chembl_results['data'][0]['output']['object']['id'][len("umls.compound") + 1:]
        else:
            return None 

if __name__ == '__main__':

    print('tests/query_desc_test_data.json', 'ChEMBL:154',
                      QueryMyChem().get_chemical_substance_description('ChEMBL:154'))
    print('tests/query_desc_test_data.json', 'ChEMBL:20883',
                      QueryMyChem().get_chemical_substance_description('ChEMBL:20883'))   # no definition field
    print('tests/query_desc_test_data.json', 'ChEMBL:110101020',
                      QueryMyChem().get_chemical_substance_description('ChEMBL:110101020'))   # wrong id
    print('tests/query_desc_test_data.json', 'ChEMBL:20883',
                      QueryMyChem().get_cui('ChEMBL:20883'))
    print('tests/query_desc_test_data.json', 'ChEMBL:20883',
                      QueryMyChem().get_mesh_id('ChEMBL:20883'))
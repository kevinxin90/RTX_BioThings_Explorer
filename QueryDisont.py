import requests
import sys

from QueryBioThingsExplorer import QueryBioThingsExplorer

class QueryDisont:

    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()

    def query_disont_to_child_disonts_desc(self, disont_id):
        disont_id = disont_id.split(':')[-1]
        disont_results = self.biothings_explorer.send_query_get(input_prefix='do', output_prefix="do", input_value=disont_id)
        ret_dict = dict()
        if disont_results:
            ret_dict = {('DOID:' + _doc['output']['object']['id'].split(':')[-1]): _doc['output']['object']['label'] for _doc in disont_results['data'] if _doc['predicate'] == "DiseaseOntologyToChildDiseaseOntologyAssociation"}
        return ret_dict

    def query_disont_to_label(self, disont_id):
        disont_id = disont_id.split(':')[-1]
        disont_results = self.biothings_explorer.send_query_get(input_prefix='do', output_prefix="diseasename", input_value=disont_id)
        if disont_results:
            return disont_results['data'][0]['output']['object']['id'].split(':')[-1]
        else:
            return None

    def query_disont_to_mesh_id(self, disont_id):
        disont_id = disont_id.split(':')[-1]
        disont_results = self.biothings_explorer.send_query_get(input_prefix='do', output_prefix="mesh.disease", input_value=disont_id)
        if disont_results:
            return set([_doc['output']['object']['id'].split(':')[-1] for _doc in disont_results['data']])
        else:
            return set()

if __name__ == '__main__':
    print(QueryDisont().query_disont_to_label("DOID:0050741"))
    print(QueryDisont().query_disont_to_mesh_id("DOID:9352"))
    print(QueryDisont().query_disont_to_mesh_id("DOID:1837"))
    print(QueryDisont().query_disont_to_mesh_id("DOID:10182"))
    print(QueryDisont().query_disont_to_mesh_id("DOID:11712"))
    print(QueryDisont().query_disont_to_child_disonts_desc("DOID:9352"))
    print(QueryDisont().query_disont_to_mesh_id("DOID:14069"))
    print(QueryDisont().query_disont_to_child_disonts_desc("DOID:12365"))
    print(QueryDisont().query_disont_to_mesh_id("DOID:0050741"))
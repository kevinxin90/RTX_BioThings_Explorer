from QueryBioThingsExplorer import QueryBioThingsExplorer

class QueryEBIOLS:

    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()

    def get_mesh_id_for_uberon_id(self, uberon_curie_id):
    	anatomy_value = uberon_curie_id.split(':')[1]
    	ols_results = self.biothings_explorer.send_query_get(input_prefix='uberon', output_prefix="mesh.anatomy", input_value=anatomy_value)
    	if ols_results:
    		mesh_id = set(_doc['output']['object']['id'].replace('mesh.anatomy', 'MESH') for _doc in ols_results['data'])
    		return mesh_id
    	else:
    		return None

if __name__ == "__main__":
#    print(QueryEBIOLS.send_query_get("uberon/terms/" + urllib.parse.quote_plus(urllib.parse.quote_plus("http://purl.obolibrary.org/obo/UBERON_0002107")), ""))
    print(QueryEBIOLS().get_mesh_id_for_uberon_id("UBERON:0002107"))
    print(QueryEBIOLS().get_mesh_id_for_uberon_id("UBERON:0001162"))
    
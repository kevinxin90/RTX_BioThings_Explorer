from QueryBioThingsExplorer import QueryBioThingsExplorer


class QueryPC2:
    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()

    def pathway_id_to_uniprot_ids(self, pathway_reactome_id):
        mygene_results = self.biothings_explorer.send_query_get(input_prefix='reactome.pathway',
                                                                output_prefix="ncbigene",
                                                                input_value=pathway_reactome_id)
        res_set = set()
        if mygene_results:
            ncbigene_ids = set([_doc['output']['object']['id'].split(':')[-1] for _doc in mygene_results['data']])
            for geneid in ncbigene_ids:
                mygene_uniprot_results = self.biothings_explorer.send_query_get(input_prefix='ncbigene',
                                                                                output_prefix="uniprot",
                                                                                input_value=geneid)
                if mygene_uniprot_results:
                    for uniprot_doc in mygene_uniprot_results['data']:
                        res_set.add(uniprot_doc['output']['object']['id'].split(':')[-1])
        return res_set

    def uniprot_id_to_reactome_pathways(self, uniprot_id):
        mygene_results = self.biothings_explorer.send_query_get(input_prefix='uniprot', output_prefix="ncbigene",
                                                                input_value=uniprot_id)
        pathway_set = set()
        if mygene_results:
            ncbigene_ids = set([_doc['output']['object']['id'].split(':')[-1] for _doc in mygene_results['data'] if
                                'taxonomy' in _doc['output']['object'] and _doc['output']['object'][
                                    'taxonomy'] == '9606'])
            for ncbigene_id in ncbigene_ids:
                mygene_pathway_results = self.biothings_explorer.send_query_get(input_prefix='ncbigene',
                                                                                output_prefix="reactome.pathway",
                                                                                input_value=ncbigene_id)
                if mygene_pathway_results:
                    for reactome_doc in mygene_pathway_results['data']:
                        pathway_set.add(reactome_doc['output']['object']['id'].split(':')[-1])
        return pathway_set


if __name__ == '__main__':
    print(QueryPC2().uniprot_id_to_reactome_pathways("P68871"))
    print(QueryPC2().pathway_id_to_uniprot_ids("R-HSA-2168880"))

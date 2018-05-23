from QueryBioThingsExplorer import QueryBioThingsExplorer

class QueryChEMBL:

    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()

    def get_chembl_ids_for_drug(self, drug_name):
        chembl_results = self.biothings_explorer.send_query_get(input_prefix='drugname', output_prefix="chembl.compound", input_value=drug_name)
        if chembl_results:
            res_chembl_set = set([_doc['output']['object']['id'].split(':')[-1] for _doc in chembl_results['data'] if _doc['endpoint'] == "https://www.ebi.ac.uk/chembl/api/data/compound_record"])
            return res_chembl_set
        else:
            return None

    def get_target_uniprot_ids_for_chembl_id(self, chembl_id):
        target_predictions_list = self.biothings_explorer.send_query_get(input_prefix='chembl.compound', output_prefix='uniprot', input_value=chembl_id)
        res_targets_dict = dict()
        res_targets_dict = {_doc['output']['object']['id'].split(":")[1]: float(_doc['output']['edge']['probability']) for _doc in target_predictions_list['data'] if 'edge' in _doc['output'] and
                            'probability' in _doc['output']['edge'] and _doc['output']['object']['taxonomy']=='9606'}
        return res_targets_dict

    def get_target_uniprot_ids_for_drug(self, drug_name):
        chembl_ids_for_drug = QueryChEMBL().get_chembl_ids_for_drug(drug_name)
        res_uniprot_ids = dict()
        if chembl_ids_for_drug:
            for chembl_id in chembl_ids_for_drug:
    #            print(chembl_id)
                uniprot_ids_dict = self.get_target_uniprot_ids_for_chembl_id(chembl_id)
                if uniprot_ids_dict:
                    for uniprot_id in uniprot_ids_dict.keys():
                        res_uniprot_ids[uniprot_id] = uniprot_ids_dict[uniprot_id]
            return res_uniprot_ids
        else:
            return res_uniprot_ids
    
    def test(self):
        print(QueryChEMBL().get_chembl_ids_for_drug('lovastatin'))
        print(QueryChEMBL().get_chembl_ids_for_drug('acetaminophen'))
        print(QueryChEMBL().get_target_uniprot_ids_for_drug('clothiapine'))
        
if __name__ == '__main__':
    QueryChEMBL().test()
    
    
    

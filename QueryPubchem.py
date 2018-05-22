import requests
import sys

from QueryBioThingsExplorer import QueryBioThingsExplorer

class QueryPubChem:

    def __init__(self):
        self.biothings_explorer = QueryBioThingsExplorer()

    def get_chembl_ids_for_drug(self, drug_name):
        mychem_results = self.biothings_explorer.send_query_get(input_prefix='drugname', output_prefix="drugname", input_value=drug_name)
        if mychem_results:
            chembl_ids = set([_doc['output']['object']['id'].split(':')[-1] for _doc in mychem_results['data'] if _doc['output']['object']['id'].startswith('drugname:CHEMBL')])
            return chembl_ids
        else:
            return set()

    def get_pubchem_id_for_chembl_id(self, chembl_id):
        mychem_results = self.biothings_explorer.send_query_get(input_prefix='chembl.compound', output_prefix="pubchem.compound", input_value=chembl_id)
        if mychem_results:
            pubchem_ids = set([_doc['output']['object']['id'].split(':')[-1] for _doc in mychem_results['data'] if not _doc['output']['object']['id'].startswith('pubchem.compound:CID')])
            return pubchem_ids
        else:
            return set()

    def get_pubmed_id_for_pubchem_id(self, pubchem_id):
        pubchem_results = self.biothings_explorer.send_query_get(input_prefix='pubchem.compound', output_prefix="pubmed", input_value=pubchem_id)
        if pubchem_results:
            pubmed_ids = [_doc['output']['object']['id'].split(':')[-1] for _doc in pubchem_results['data']]
            return pubmed_ids
        else:
            return None
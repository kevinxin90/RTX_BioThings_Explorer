def convert_gene_symbol_to_uniprot_id(self, gene_symbol):
    res = QueryBioThingsExplorer().send_query_get(input_prefix='hgnc.symbol', 
    											  output_prefix="uniprot", 
    											  input_value=gene_symbol)
    uniprot_ids = set([_doc['output']['object']['id'] for _doc in res['data']])
    return uniprot_ids
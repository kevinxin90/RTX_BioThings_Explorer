__all__ = ['convert_rtx_curie_id_to_bt_explorer_input']

_input_prefix_map = {
    # metabolite
    "KEGG": "kegg.compound",
    # protein
    "UniProtKB": "uniprot",
    # anatomical_entity
    "UBERON": "uberon",
    # TODO category?
    "CL": "cl",
    # gene_ontolog
    "GO": "go",
    # disease
    "DOID": "do",
    # genetic_condition
    "OMIM": "omim.disease",
    # phenotypic_feature
    "HP": "hp",
    # "AQTLTrait": None,
    # microRNA
    "NCBIGene": "ncbigene",
    # pathway
    "REACT": "reactome.pathway",
    # checmical_substance
    "ChEMBL": "chembl.compound"
}


def convert_rtx_curie_id_to_bt_explorer_input(curie_id):
    """
    KEGG --> ^C\d+$, equivalent to splitting by colon. E.g. "KEGG:C123" --> "C123"
    UniProtKB --> split by colon; use the second part as input value
    UBERON --> as is
    CL --> as is (e.g "CL:0000492")
    GO --> as is
    DOID --> split by colon; use the second part as input value (Not compatible with identifiers.org)
    OMIM --> split by colon; use the second part as input value
    HP --> as is
    NCBIGene --> split bycolon; use the second part as input value
    REACT --> split bycolon; use the second part as input value
    ChEMBL --> ^CHEMBL\d+$, e.g. "ChEMBL:123" --> "CHEMBL123"
    """

    curie_prefix, curie_value = curie_id.split(":")
    if curie_prefix in {"KEGG", "UniProtKB", "DOID", "OMIM", "NCBIGene", "REACT"}:
        bte_input_value = curie_value
    elif curie_prefix == "ChEMBL":
        bte_input_value = "CHEMBL" + curie_value
    else:
        bte_input_value = curie_id  # as is

    bte_input_prefix = _input_prefix_map.get(curie_prefix, None)
    if bte_input_prefix is None:
        raise ValueError("Cannot find BioThings Explorer prefix for curie prefix {}".format(curie_prefix))

    return bte_input_prefix, bte_input_value

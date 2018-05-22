import unittest
import RTXCurieUtil as rcu


class RTXCurieUtilTestCase(unittest.TestCase):
    def test_convert_rtx_curie_id_to_bt_explorer_input(self):
        test_data = {
            "KEGG:C00022": ("kegg.compound", "C00022"),
            "UniProtKB:P01358": ("uniprot", "P01358"),
            "UBERON:0004476": ("uberon", "UBERON:0004476"),
            "CL:0000492": ("cl", "CL:0000492"),
            "GO:0097289": ("go", "GO:0097289"),
            "DOID:3965": ("do", "DOID:3965"),
            "OMIM:100100": ("omim.disease", "100100"),
            "HP:0011515": ("hp", "HP:0011515"),
            "NCBIGene:1008470860": ("ncbigene", "1008470860"),
            "REACT:R-HSA-703260": ("reactome.pathway", "R-HSA-703260"),
            "ChEMBL:1200766": ("chembl.compound", "CHEMBL1200766")
        }

        for input, output in test_data.items():
            self.assertEqual(rcu.convert_rtx_curie_id_to_bt_explorer_input(input), output),


if __name__ == '__main__':
    unittest.main()

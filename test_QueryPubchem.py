import unittest
from QueryPubchem import QueryPubChem


class QueryPubChemTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pc = QueryPubChem()

    def test_get_chembl_ids_for_drug(self):
        # bte_result = self.pc.get_chembl_ids_for_drug("acetaminophen")
        # rtx_result = {'CHEMBL112'}
        # self.assertSetEqual(bte_result, rtx_result)

        # bte_result = self.pc.get_chembl_ids_for_drug("lovastatin")
        # rtx_result = {'CHEMBL503'}
        # self.assertSetEqual(bte_result, rtx_result)

        self.skipTest("Not implemented. Use QueryChEMBL::get_chembl_ids_for_drug instead.")

    def test_get_pubchem_id_for_chembl_id(self):
        bte_result = self.pc.get_pubchem_id_for_chembl_id("CHEMBL503")
        # BioThings Explorer API returns a set of chembl IDs
        bte_result = next(iter(bte_result))
        rtx_result = '53232'
        self.assertEqual(bte_result, rtx_result)

    def test_get_pubmed_id_for_pubchem_id(self):
        bte_result = self.pc.get_pubmed_id_for_pubchem_id("53232")
        rtx_result_len = 2600
        # TODO: Will get an extremely long list here, so only the lengths are compared
        self.assertEqual(len(bte_result), rtx_result_len)


if __name__ == '__main__':
    unittest.main()

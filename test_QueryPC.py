import unittest
from QueryPC import QueryPC2


class QueryPCTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pc = QueryPC2()

    def test_pathway_id_to_uniprot_ids(self):
        # bte_result = self.pc.pathway_id_to_uniprot_ids("R-HSA-2168880")
        # rtx_result = set()
        # self.assertSetEqual(bte_result, rtx_result)

        # bte_result = self.pc.pathway_id_to_uniprot_ids("R-HSA-2168878")
        # rtx_result = set()
        # self.assertSetEqual(bte_result, rtx_result)
        self.skipTest("Bug on RTX side. See https://github.com/RTXteam/RTX/issues/226")

    def test_uniprot_id_to_reactome_pathways(self):
        # bte_result = self.pc.uniprot_id_to_reactome_pathways("P68871")
        # rtx_result = {'R-HSA-109582',
        #               'R-HSA-1480926',
        #               'R-HSA-168249',
        #               'R-HSA-168256',
        #               'R-HSA-2173782',
        #               'R-HSA-382551',
        #               'R-HSA-5653656'}
        # self.assertSetEqual(bte_result, rtx_result)
        #
        # bte_result = self.pc.uniprot_id_to_reactome_pathways("P12345")
        # rtx_result = {}
        # self.assertSetEqual(bte_result, rtx_result)
        self.skipTest("Function logic in doubt. See https://github.com/kevinxin90/RTX_BioThings_Explorer/issues/1")


if __name__ == '__main__':
    unittest.main()

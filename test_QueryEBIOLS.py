import unittest
from QueryEBIOLS import QueryEBIOLS


class QueryEBIOLSTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ebiols = QueryEBIOLS()

    def test_get_mesh_id_for_uberon_id(self):
        bte_result = self.ebiols.get_mesh_id_for_uberon_id("UBERON:0002107")
        rtx_result = {'MESH:D008099'}
        self.assertSetEqual(bte_result, rtx_result)

        bte_result = self.ebiols.get_mesh_id_for_uberon_id("UBERON:0001162")
        rtx_result = {'MESH:A03.492.766.163'}
        self.assertSetEqual(bte_result, rtx_result)


if __name__ == '__main__':
    unittest.main()

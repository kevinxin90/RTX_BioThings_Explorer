import unittest
from QueryDisont import QueryDisont


class QueryDisontTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.disont = QueryDisont()

    def test_query_disont_to_child_disonts(self):
        bte_result = self.disont.query_disont_to_child_disonts("DOID:9352")
        rtx_result = {1837, 10182, 11712}
        self.assertSetEqual(bte_result, rtx_result)

        bte_result = self.disont.query_disont_to_child_disonts("DOID:12365")
        rtx_result = {12919, 12978, 14067, 14068, 14069, 14324, 14325}
        self.assertSetEqual(bte_result, rtx_result)

    def test_query_disont_to_child_disonts_desc(self):
        # TODO: RTX gets {'DOID:11712': 'lipoatrophic diabetes'} while BioThings Explorer gets {'DOID:11712': 'lipoatrophic diabetes mellitus'}

        # bte_result = self.disont.query_disont_to_child_disonts_desc("DOID:9352")
        # rtx_result = {'DOID:10182': 'diabetic peripheral angiopathy',
        #               'DOID:11712': 'lipoatrophic diabetes',
        #               'DOID:1837': 'diabetic ketoacidosis'}
        # print(bte_result)
        # self.assertEqual(len(bte_result), len(rtx_result))
        # for key, value in bte_result.items():
        #     self.assertEqual(rtx_result[key], value)

        bte_result = self.disont.query_disont_to_child_disonts_desc("DOID:12365")
        rtx_result = {'DOID:12919': 'Plasmodium ovale malaria',
                      'DOID:12978': 'Plasmodium vivax malaria',
                      'DOID:14067': 'Plasmodium falciparum malaria',
                      'DOID:14068': 'blackwater fever',
                      'DOID:14069': 'cerebral malaria',
                      'DOID:14324': 'Plasmodium malariae malaria',
                      'DOID:14325': 'mixed malaria'}
        self.assertEqual(len(bte_result), len(rtx_result))
        for key, value in bte_result.items():
            self.assertEqual(rtx_result[key], value)

    def test_query_disont_to_label(self):
        bte_result = self.disont.query_disont_to_label("DOID:0050741")
        rtx_result = 'alcohol dependence'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.disont.query_disont_to_label("DOID:12365")
        rtx_result = 'malaria'
        self.assertEqual(bte_result, rtx_result)

    def test_query_disont_to_mesh_id(self):
        bte_result = self.disont.query_disont_to_mesh_id("DOID:9352")
        rtx_result = {'D003924'}
        self.assertSetEqual(bte_result, rtx_result)

        bte_result = self.disont.query_disont_to_mesh_id("DOID:1837")
        rtx_result = {'D016883'}
        self.assertSetEqual(bte_result, rtx_result)


if __name__ == '__main__':
    unittest.main()

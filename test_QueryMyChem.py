import unittest
from QueryMyChem import QueryMyChem


class QueryMyChemTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mc = QueryMyChem()

    def test_get_chemical_substance_entity(self):
        self.skip("Not implemented because it's not a general-purpose method to BioThings Explorer")

    def test_get_chemical_substance_description(self):
        bte_result = self.mc.get_chemical_substance_description("ChEMBL:154")
        rtx_result = 'A methoxynaphthalene that is 2-methoxynaphthalene substituted by a carboxy ethyl group at ' \
                     'position 6. Naproxen is a non-steroidal anti-inflammatory drug commonly used for the reduction ' \
                     'of pain, fever, inflammation  and stiffness caused by conditions such as osteoarthritis, ' \
                     'kidney stones, rheumatoid arthritis, psoriatic arthritis, gout, ankylosing spondylitis, ' \
                     'menstrual cramps, tendinitis, bursitis, and for the treatment of primary dysmenorrhea. It works ' \
                     'by inhibiting both the COX-1 and COX-2 enzymes.'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.mc.get_chemical_substance_description("ChEMBL:20883")  # no definition field
        rtx_result = 'None'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.mc.get_chemical_substance_description("ChEMBL:110101020")  # wrong id
        rtx_result = 'None'
        self.assertEqual(bte_result, rtx_result)

    def test_get_mesh_id(self):
        bte_result = self.mc.get_mesh_id("ChEMBL:154")
        rtx_result = 'D009288'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.mc.get_mesh_id("ChEMBL:20883")
        rtx_result = 'D005641'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.mc.get_mesh_id("ChEMBL:110101020")  # wrong id
        rtx_result = None
        self.assertEqual(bte_result, rtx_result)

    def test_get_cui(self):
        bte_result = self.mc.get_cui("ChEMBL:154")
        rtx_result = 'C0027396'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.mc.get_cui("ChEMBL:20883")
        rtx_result = 'C0016778'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.mc.get_cui("ChEMBL:110101020")  # wrong id
        rtx_result = None
        self.assertEqual(bte_result, rtx_result)


if __name__ == '__main__':
    unittest.main()

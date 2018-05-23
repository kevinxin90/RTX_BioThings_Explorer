import unittest
from QueryEBIOLSExtended import QueryEBIOLSExtended


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ebiols = QueryEBIOLSExtended()

    def test_get_anatomy_description(self):
        bte_result = self.ebiols.get_anatomy_description("UBERON:0004476")
        rtx_result = 'The collection of muscles that form attachments to the shoulder skeleton.'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.ebiols.get_anatomy_description("UBERON:00044760")
        rtx_result = 'None'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.ebiols.get_anatomy_description("CL:0000038")
        rtx_result = 'A progenitor cell committed to the erythroid lineage.'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.ebiols.get_anatomy_description("CL:00000380")
        rtx_result = 'None'
        self.assertEqual(bte_result, rtx_result)

    def test_get_bio_process_description(self):
        # bte_result = self.ebiols.get_bio_process_description("GO:0042535")
        # rtx_result = 'Any process that activates or increases the frequency, rate or extent; of the chemical ' \
        #              'reactions and pathways resulting in the formation of tumor necro; sis factor, an inflammatory ' \
        #              'cytokine produced by macrophages/monocytes during ac; ute inflammation and which is responsible ' \
        #              'for a diverse range of signaling event; s within cells, leading to necrosis or apoptosis. '
        # self.assertEqual(bte_result, rtx_result)

        bte_result = self.ebiols.get_bio_process_description("GO:00425350")
        rtx_result = 'None'
        self.assertEqual(bte_result, rtx_result)


if __name__ == '__main__':
    unittest.main()

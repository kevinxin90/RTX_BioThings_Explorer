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
        bte_result = self.ebiols.get_bio_process_description("GO:0042535")
        rtx_result = 'Any process that activates or increases the frequency, rate or extent of the chemical reactions ' \
                     'and pathways resulting in the formation of tumor necrosis factor, an inflammatory cytokine ' \
                     'produced by macrophages/monocytes during acute inflammation and which is responsible for a ' \
                     'diverse range of signaling events within cells, leading to necrosis or apoptosis. '

        self.assertEqual(bte_result, rtx_result)

        bte_result = self.ebiols.get_bio_process_description("GO:00425350")
        rtx_result = 'None'
        self.assertEqual(bte_result, rtx_result)

    def test_get_phenotype_description(self):
        bte_result = self.ebiols.get_phenotype_description("HP:0011105")
        rtx_result = 'An increase in the amount of intravascular fluid, particularly in the volume of the circulating ' \
                     'blood.'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.ebiols.get_phenotype_description("HP:00111050")
        rtx_result = 'None'
        self.assertEqual(bte_result, rtx_result)

    def test_get_disease_description(self):
        # bte_result = self.ebiols.get_disease_description('OMIM:613573')
        # rtx_result = 'None'
        # self.assertEqual(bte_result, rtx_result)
        #
        # bte_result = self.ebiols.get_disease_description('OMIM:6135730')
        # rtx_result = 'None'
        # self.assertEqual(bte_result, rtx_result)

        self.skipTest("Kevin claimed that OMIM is not ontology (but we are using API for ontologies) and suggested "
                      "use MONDO instead")

    def test_get_cellular_component_description(self):
        bte_result = self.ebiols.get_cellular_component_description('GO:0005573')
        rtx_result = 'OBSOLETE (was not defined before being made obsolete).'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.ebiols.get_cellular_component_description('GO:00055730')
        rtx_result = 'None'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.ebiols.get_cellular_component_description('GO:0005575')
        rtx_result = 'A location, relative to cellular compartments and structures, occupied by a macromolecular ' \
                     'machine when it carries out a molecular function. There are two ways in which the gene ontology ' \
                     'describes locations of gene products: (1) relative to cellular structures (e.g., cytoplasmic ' \
                     'side of plasma membrane) or compartments (e.g., mitochondrion), and (2) the stable ' \
                     'macromolecular complexes of which they are parts (e.g., the ribosome).'
        self.assertEqual(bte_result, rtx_result)

    def test_get_molecular_function_description(self):
        bte_result = self.ebiols.get_cellular_component_description('GO:0004689')
        rtx_result = 'Catalysis of the reaction: 4 ATP + 2 phosphorylase b = 4 ADP + phosphorylase a.'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.ebiols.get_cellular_component_description('GO:00046890')
        rtx_result = 'None'
        self.assertEqual(bte_result, rtx_result)

if __name__ == '__main__':
    unittest.main()

import unittest
from QueryMyGene import QueryMyGene


class QueryMyGeneTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mg = QueryMyGene()

    def test_convert_uniprot_id_to_gene_symbol(self):
        bte_result = self.mg.convert_uniprot_id_to_gene_symbol('Q8NBZ7')
        rtx_result = {'UXS1'}
        self.assertSetEqual(bte_result, rtx_result)

        bte_result = self.mg.convert_uniprot_id_to_gene_symbol('P12345')
        rtx_result = set()
        self.assertSetEqual(bte_result, rtx_result)

    def test_get_gene_ontology_ids_bp_for_uniprot_id(self):
        bte_result = self.mg.get_gene_ontology_ids_bp_for_uniprot_id('Q05925')
        rtx_result = {'GO:0000122': 'negative regulation of transcription by RNA polymerase II',
                      'GO:0001501': 'skeletal system development',
                      'GO:0008344': 'adult locomotory behavior',
                      'GO:0009653': 'anatomical structure morphogenesis',
                      'GO:0009953': 'ventral pattern formation',
                      'GO:0009954': 'distal pattern formation',
                      'GO:0021549': 'cerebellum development',
                      'GO:0030901': 'midbrain development',
                      'GO:0030917': 'midbrain-hindbrain boundary development',
                      'GO:0035115': 'embryonic forelimb morphogenesis',
                      'GO:0035176': 'social behavior',
                      'GO:0035264': 'multicellular organism growth',
                      'GO:0042756': 'drinking behavior',
                      'GO:0043473': 'pigmentation',
                      'GO:0043524': 'negative regulation of neuron apoptotic process',
                      'GO:0045944': 'positive regulation of transcription by RNA polymerase II',
                      'GO:0048666': 'neuron development',
                      'GO:0061743': 'motor learning',
                      'GO:0071542': 'dopaminergic neuron differentiation',
                      'GO:1990403': 'embryonic brain development'}
        self.assertDictEqual(bte_result, rtx_result)

        bte_result = self.mg.get_gene_ontology_ids_bp_for_uniprot_id('Q8NBZ7')
        rtx_result = {'GO:0033320': 'UDP-D-xylose biosynthetic process',
                      'GO:0051262': 'protein tetramerization'}
        self.assertDictEqual(bte_result, rtx_result)

    def test_uniprot_id_is_human(self):
        bte_result = self.mg.uniprot_id_is_human("P02794")
        rtx_result = True
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.mg.uniprot_id_is_human("P10592")
        rtx_result = False
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.mg.uniprot_id_is_human("P12345")
        rtx_result = False
        self.assertEqual(bte_result, rtx_result)

    def test_convert_entrez_gene_ID_to_mirbase_ID(self):
        bte_result = self.mg.convert_entrez_gene_ID_to_mirbase_ID(407053)
        rtx_result = {'MI0000098'}
        self.assertSetEqual(bte_result, rtx_result)

        bte_result = self.mg.convert_entrez_gene_ID_to_mirbase_ID(12345)  # Not a human gene
        rtx_result = set()
        self.assertEqual(bte_result, rtx_result)

    def test_get_gene_ontology_ids_bp_for_entrez_gene_id(self):
        bte_result = self.mg.get_gene_ontology_ids_bp_for_entrez_gene_id(407053)
        rtx_result = {'GO:0035278': 'miRNA mediated inhibition of translation',
                      'GO:1904706': 'negative regulation of vascular smooth muscle cell proliferation'}
        self.assertDictEqual(bte_result, rtx_result)

        # bte_result = self.mg.get_gene_ontology_ids_bp_for_entrez_gene_id(12345)  # Not a human gene
        # rtx_result = dict()
        # self.assertDictEqual(bte_result, rtx_result)  # TODO: BTE does not specify species to human

    def test_convert_gene_symbol_to_uniprot_id(self):
        bte_result = self.mg.convert_gene_symbol_to_uniprot_id('A2M')
        rtx_result = {'P01023'}
        self.assertSetEqual(bte_result, rtx_result)

        bte_result = self.mg.convert_gene_symbol_to_uniprot_id('A1BG')
        rtx_result = {'P04217'}
        self.assertSetEqual(bte_result, rtx_result)

        bte_result = self.mg.convert_gene_symbol_to_uniprot_id('HMOX1')
        rtx_result = {'P09601'}
        self.assertSetEqual(bte_result, rtx_result)

        bte_result = self.mg.convert_gene_symbol_to_uniprot_id('RAD54B')
        rtx_result = {'O95073', 'Q9Y620'}
        self.assertSetEqual(bte_result, rtx_result)

        bte_result = self.mg.convert_gene_symbol_to_uniprot_id('NS2')
        rtx_result = set()
        self.assertSetEqual(bte_result, rtx_result)

    def test_convert_gene_symbol_to_entrez_gene_ID(self):
        bte_result = self.mg.convert_gene_symbol_to_entrez_gene_ID('MIR96')
        rtx_result = {407053}
        self.assertSetEqual(bte_result, rtx_result)

        bte_result = self.mg.convert_gene_symbol_to_entrez_gene_ID('MIR48')
        rtx_result = set()
        self.assertSetEqual(bte_result, rtx_result)

    def test_convert_uniprot_id_to_entrez_gene_ID(self):
        bte_result = self.mg.convert_uniprot_id_to_entrez_gene_ID("P09601")
        rtx_result = {3162}
        self.assertSetEqual(bte_result, rtx_result)

        bte_result = self.mg.convert_uniprot_id_to_entrez_gene_ID("XYZZY")
        rtx_result = set()
        self.assertSetEqual(bte_result, rtx_result)


if __name__ == '__main__':
    unittest.main()

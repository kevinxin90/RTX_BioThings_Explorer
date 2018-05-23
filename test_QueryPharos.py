import unittest
from QueryPharos import QueryPharos


class QueryPharosTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pharos = QueryPharos()

    def test_query_drug_name_to_targets(self):
        # bte_result = self.pharos.query_drug_name_to_targets('paclitaxel')
        # # TODO: BioThings Explorer API can only return short names, e.g. TUBB3 for Tubulin beta-3 chain
        # # TODO: Should a target ID be an int or a string?
        # rtx_result = [{'id': 1995, 'name': 'Tubulin beta-3 chain'},
        #               {'id': 15579, 'name': 'Tubulin beta chain'},
        #               {'id': 10262, 'name': 'Tubulin beta-1 chain'},
        #               {'id': 16012, 'name': 'Cytochrome P450 3A4'},
        #               {'id': 1906, 'name': 'Tubulin beta-4A chain'},
        #               {'id': 18746, 'name': 'Cytochrome P450 3A5'},
        #               {'id': 16739, 'name': 'Mimitin, mitochondrial'},
        #               {'id': 15851, 'name': 'Tubulin beta-4B chain'},
        #               {'id': 13919, 'name': 'Ribonucleoside-diphosphate reductase large subunit'},
        #               {'id': 5762, 'name': 'Tubulin beta-2A chain'}]
        # bte_ids = {x["id"] for x in bte_result}
        # rtx_ids = {x["id"] for x in rtx_result}
        # self.assertSetEqual(set(bte_ids), set(rtx_ids))

        # bte_result = self.pharos.query_drug_name_to_targets('lovastatin')
        # rtx_result = [{'id': 19672, 'name': '3-hydroxy-3-methylglutaryl-coenzyme A reductase'},
        #               {'id': 14711, 'name': 'Integrin alpha-L'},
        #               {'id': 3939, 'name': 'Farnesyl pyrophosphate synthase'},
        #               {'id': 14764, 'name': 'Integrin beta-3'},
        #               {'id': 13844, 'name': 'Cytochrome P450 2D6'},
        #               {'id': 16824, 'name': 'Prostacyclin receptor'},
        #               {'id': 17657, 'name': 'Serine/threonine-protein kinase mTOR'},
        #               {'id': 8600, 'name': 'Prostaglandin G/H synthase 2'},
        #               {'id': 18746, 'name': 'Cytochrome P450 3A5'},
        #               {'id': 7520, 'name': 'C-C chemokine receptor type 5'}]
        # bte_ids = {x["id"] for x in bte_result}
        # rtx_ids = {x["id"] for x in rtx_result}
        # self.assertSetEqual(set(bte_ids), set(rtx_ids))

        self.skipTest('Kevin Implemented this method in a different way. Check his Google Doc.')

    def test_query_target_to_diseases(self):
        bte_result = self.pharos.query_target_to_diseases("16012")
        rtx_result = [{'id': '852', 'name': 'Hepatitis C'},
                      {'id': '35', 'name': 'osteosarcoma'},
                      {'id': '67', 'name': 'Prostatic Neoplasms'},
                      {'id': '4854', 'name': 'Torsades de Pointes'},
                      {'id': '771', 'name': 'Mammary Neoplasms'},
                      {'id': '50', 'name': 'astrocytic glioma'},
                      {'id': '51', 'name': 'ependymoma'},
                      {'id': '52', 'name': 'oligodendroglioma'},
                      {'id': '47', 'name': 'cutaneous lupus erythematosus'},
                      {'id': '42', 'name': 'psoriasis'},
                      {'id': '5', 'name': 'medulloblastoma, large-cell'},
                      {'id': '304', 'name': 'adrenocortical adenoma'},
                      {'id': '95', 'name': 'pancreatic ductal adenocarcinoma liver metastasis'},
                      {'id': '49', 'name': 'intraductal papillary-mucinous neoplasm (IPMN)'},
                      {'id': '129', 'name': 'Cancer'},
                      {'id': '849', 'name': 'Liver disease'},
                      {'id': '2102', 'name': 'Diarrhea'},
                      {'id': '745', 'name': 'Neutropenia'},
                      {'id': '1855', 'name': 'Human immunodeficiency virus infectious disease'},
                      {'id': '662', 'name': 'Exanthem'},
                      {'id': '205', 'name': 'Hypertension'},
                      {'id': '53', 'name': 'diabetes mellitus'},
                      {'id': '6190', 'name': 'Sexual dysfunction'},
                      {'id': '893', 'name': 'Leber congenital amaurosis'},
                      {'id': '349', 'name': 'Cholestasis'},
                      {'id': '300', 'name': 'Epilepsy'},
                      {'id': '203', 'name': 'Coronary artery disease'},
                      {'id': '171', 'name': 'tuberculosis'},
                      {'id': '209', 'name': 'Kidney disease'},
                      {'id': '332', 'name': 'Toxic encephalopathy'},
                      {'id': '61', 'name': 'Schizophrenia'},
                      {'id': '533', 'name': 'Pain agnosia'},
                      {'id': '9826', 'name': 'Human immunodeficiency virus infection'}]
        bte_ids = {x["id"] for x in bte_result}
        rtx_ids = {x["id"] for x in rtx_result}
        self.assertSetEqual(set(bte_ids), set(rtx_ids))

    def test_query_target_to_drugs(self):
        # bte_result = self.pharos.query_target_to_drugs("16012")
        # rtx_result = [{'action': 'INHIBITOR', 'id': 4490391, 'name': 'cobicistat'}]
        # self.assertEqual(len(bte_result), len(rtx_result))

        self.skipTest("Kevin claimed that we should use 'refid' instead of the 'Record ID'. Check his Google Doc")

    def test_query_drug_to_targets(self):
        # bte_result = self.pharos.query_drug_to_targets("254599")
        # rtx_result = list()
        # self.assertListEqual(bte_result, rtx_result)
        #
        # bte_result = self.pharos.query_drug_to_targets("218623")
        # rtx_result = [{'id': 9873512, 'name': 'HMGCR'}]
        # self.assertListEqual(bte_result, rtx_result)

        self.skipTest("Kevin claimed that we should use 'refid' instead of the 'Record ID'. Check his Google Doc")

    def test_query_target_name(self):
        bte_result = self.pharos.query_target_name("852")
        rtx_result = 'Putative uncharacterized protein ENSP00000382790'
        self.assertEqual(bte_result, rtx_result)

    def test_query_target_uniprot_accession(self):
        bte_result = self.pharos.query_target_uniprot_accession("852")
        rtx_result = 'A8MVM7'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.pharos.query_target_uniprot_accession("1")
        rtx_result = 'Q9UL59'
        self.assertEqual(bte_result, rtx_result)

    def test_query_disease_name(self):
        bte_result = self.pharos.query_disease_name("9636")
        rtx_result = 'MALARIA, SEVERE, SUSCEPTIBILITY TO'
        self.assertEqual(bte_result, rtx_result)

    def test_query_disease_id_by_name(self):
        bte_result = self.pharos.query_disease_id_by_name("MALARIA, SEVERE, SUSCEPTIBILITY TO")
        rtx_result = '936'
        self.assertEqual(bte_result, rtx_result)

    def test_query_drug_name(self):
        bte_result = self.pharos.query_drug_name("218623")
        rtx_result = 'lovastatin'
        self.assertEqual(bte_result, rtx_result)

    def test_query_drug_id_by_name(self):
        bte_result = self.pharos.query_drug_id_by_name("lovastatin")
        rtx_result = 218623
        self.assertEqual(bte_result, rtx_result)


if __name__ == '__main__':
    unittest.main()

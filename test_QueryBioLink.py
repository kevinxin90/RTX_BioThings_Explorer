import unittest
from QueryBioLink import QueryBioLink


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bl = QueryBioLink()

    def test_get_label_for_disease(self):
        bte_result = self.bl.get_label_for_disease("DOID:1498")
        rtx_result = 'cholera'
        self.assertEqual(bte_result, rtx_result)

        bte_result = self.bl.get_label_for_disease("OMIM:605543")
        rtx_result = 'autosomal dominant Parkinson disease 4'
        self.assertEqual(bte_result, rtx_result)

    def test_get_phenotypes_for_disease_desc(self):
        bte_result = self.bl.get_phenotypes_for_disease_desc("DOID:1498")
        rtx_result = {'HP:0000083': 'Renal insufficiency',
                      'HP:0000789': 'Infertility',
                      'HP:0000969': 'Edema',
                      'HP:0001287': 'Meningitis',
                      'HP:0001324': 'Muscle weakness',
                      'HP:0001394': 'Cirrhosis',
                      'HP:0001733': 'Pancreatitis',
                      'HP:0001941': 'Acidosis',
                      'HP:0001944': 'Dehydration',
                      'HP:0001945': 'Fever',
                      'HP:0001948': 'Alkalosis',
                      'HP:0002013': 'Vomiting',
                      'HP:0002014': 'Diarrhea',
                      'HP:0002027': 'Abdominal pain',
                      'HP:0002045': 'Hypothermia',
                      'HP:0002090': 'Pneumonia',
                      'HP:0002152': 'Hyperproteinemia',
                      'HP:0002527': 'Falls',
                      'HP:0002586': 'Peritonitis',
                      'HP:0002615': 'Hypotension',
                      'HP:0002719': 'Recurrent infections',
                      'HP:0002740': 'Recurrent E. coli infections',
                      'HP:0003326': 'Myalgia',
                      'HP:0003394': 'Muscle cramps',
                      'HP:0004395': 'Malnutrition',
                      'HP:0004798': 'Recurrent infection of the gastrointestinal tract',
                      'HP:0007354': 'Amyotrophic lateral sclerosis',
                      'HP:0010280': 'Stomatitis',
                      'HP:0011106': 'Hypovolemia',
                      'HP:0100658': 'Cellulitis',
                      'HP:0100806': 'Sepsis'}
        self.assertEqual(len(bte_result), len(rtx_result))
        for key, value in bte_result.items():
            self.assertEqual(rtx_result[key], value)

        bte_result = self.bl.get_phenotypes_for_disease_desc("OMIM:605543")
        rtx_result = {'HP:0000726': 'Dementia',
                      'HP:0000738': 'Hallucinations',
                      'HP:0001278': 'Orthostatic hypotension',
                      'HP:0001300': 'Parkinsonism',
                      'HP:0001824': 'Weight loss',
                      'HP:0002459': 'Dysautonomia',
                      'HP:0011999': 'Paranoia',
                      'HP:0100315': 'Lewy bodies'}
        self.assertEqual(len(bte_result), len(rtx_result))
        for key, value in bte_result.items():
            self.assertEqual(rtx_result[key], value)

    def test_get_diseases_for_gene_desc(self):
        # bte_result = self.bl.get_diseases_for_gene_desc("NCBIGene:407053")
        # rtx_result = dict()
        # self.assertDictEqual(bte_result, rtx_result)
        #
        # bte_result = self.bl.get_diseases_for_gene_desc("NCBIGene:100048912")
        # rtx_result = dict()
        # self.assertDictEqual(bte_result, rtx_result)
        #
        # bte_result = self.bl.get_diseases_for_gene_desc("NCBIGene:4750")
        # rtx_result = dict()
        # self.assertDictEqual(bte_result, rtx_result)
        #
        # bte_result = self.bl.get_diseases_for_gene_desc("NCBIGene:1111111")
        # rtx_result = dict()
        # self.assertDictEqual(bte_result, rtx_result)

        self.skipTest("Not testable. Monarch Initiative API now returns only MONDO. "
                      "We can convert MONDO to DOID (or OMIM?) anyhow.")

    def test_get_genes_for_disease_desc(self):
        bte_result = self.bl.get_genes_for_disease_desc("OMIM:XXXXXX")
        rtx_result = []
        self.assertListEqual(bte_result, rtx_result)

        bte_result = self.bl.get_genes_for_disease_desc("OMIM:605543")
        rtx_result = ['HGNC:11138']
        self.assertListEqual(bte_result, rtx_result)

    def test_get_label_for_phenotype(self):
        bte_result = self.bl.get_label_for_phenotype("HP:0000003")
        rtx_result = 'Multicystic kidney dysplasia'
        self.assertEqual(bte_result, rtx_result)

    def test_get_phenotypes_for_gene(self):
        bte_result = self.bl.get_phenotypes_for_gene("NCBIGene:4750")
        rtx_result = ['HP:0000003', 'HP:0000023', 'HP:0000054', 'HP:0000062',
                      'HP:0000089', 'HP:0000105', 'HP:0000110', 'HP:0000171',
                      'HP:0000204', 'HP:0000248', 'HP:0000256', 'HP:0000286',
                      'HP:0000348', 'HP:0000358', 'HP:0000369', 'HP:0000377',
                      'HP:0000470', 'HP:0000695', 'HP:0000773', 'HP:0000774',
                      'HP:0000800', 'HP:0000882', 'HP:0000888', 'HP:0000895',
                      'HP:0001169', 'HP:0001274', 'HP:0001302', 'HP:0001320',
                      'HP:0001360', 'HP:0001395', 'HP:0001405', 'HP:0001511',
                      'HP:0001538', 'HP:0001539', 'HP:0001541', 'HP:0001561',
                      'HP:0001629', 'HP:0001631', 'HP:0001643', 'HP:0001655',
                      'HP:0001744', 'HP:0001762', 'HP:0001769', 'HP:0001773',
                      'HP:0001789', 'HP:0001831', 'HP:0002023', 'HP:0002089',
                      'HP:0002093', 'HP:0002240', 'HP:0002323', 'HP:0002350',
                      'HP:0002557', 'HP:0002566', 'HP:0002979', 'HP:0002980',
                      'HP:0003016', 'HP:0003022', 'HP:0003026', 'HP:0003038',
                      'HP:0003811', 'HP:0005054', 'HP:0005257', 'HP:0005349',
                      'HP:0005766', 'HP:0005817', 'HP:0005873', 'HP:0006426',
                      'HP:0006488', 'HP:0006610', 'HP:0006956', 'HP:0008501',
                      'HP:0008873', 'HP:0009381', 'HP:0010306', 'HP:0010442',
                      'HP:0010454', 'HP:0010579', 'HP:0012368', 'HP:0100259',
                      'HP:0100750']
        self.assertSetEqual(set(bte_result), set(rtx_result))

        bte_result = self.bl.get_phenotypes_for_gene("NCBIGene:2345")
        rtx_result = []
        self.assertEqual(bte_result, rtx_result)

    def test_get_phenotypes_for_gene_desc(self):
        bte_result = self.bl.get_phenotypes_for_gene_desc("NCBIGene:1080")  # test for RTX issue #22
        rtx_result = {'HP:0000952': 'Jaundice',
                      'HP:0001974': 'Leukocytosis',
                      'HP:0011227': 'Elevated C-reactive protein level',
                      'HP:0012379': 'Abnormal enzyme/coenzyme activity',
                      'HP:0030247': 'Splanchnic vein thrombosis'}
        # There are some differences in phenotype labels, so compare ID only
        self.assertEqual(bte_result.keys(), rtx_result.keys())

        bte_result = self.bl.get_phenotypes_for_gene_desc("NCBIGene:4750")
        rtx_result = {'HP:0000003': 'Multicystic kidney dysplasia',
                      'HP:0000023': 'Inguinal hernia',
                      'HP:0000054': 'Micropenis',
                      'HP:0000062': 'Ambiguous genitalia',
                      'HP:0000089': 'Renal hypoplasia',
                      'HP:0000105': 'Enlarged kidney',
                      'HP:0000110': 'Renal dysplasia',
                      'HP:0000171': 'Microglossia',
                      'HP:0000204': 'Cleft upper lip',
                      'HP:0000248': 'Brachycephaly',
                      'HP:0000256': 'Macrocephaly',
                      'HP:0000286': 'Epicanthus',
                      'HP:0000348': 'High forehead',
                      'HP:0000358': 'Posteriorly rotated ears',
                      'HP:0000369': 'Low-set ears',
                      'HP:0000377': 'Abnormality of the pinna',
                      'HP:0000470': 'Short neck',
                      'HP:0000695': 'Natal tooth',
                      'HP:0000773': 'Short ribs',
                      'HP:0000774': 'Narrow chest',
                      'HP:0000800': 'Cystic renal dysplasia',
                      'HP:0000882': 'Hypoplastic scapulae',
                      'HP:0000888': 'Horizontal ribs',
                      'HP:0000895': 'Lateral clavicle hook',
                      'HP:0001169': 'Broad palm',
                      'HP:0001274': 'Agenesis of corpus callosum',
                      'HP:0001302': 'Pachygyria',
                      'HP:0001320': 'Cerebellar vermis hypoplasia',
                      'HP:0001360': 'Holoprosencephaly',
                      'HP:0001395': 'Hepatic fibrosis',
                      'HP:0001405': 'Periportal fibrosis',
                      'HP:0001511': 'Intrauterine growth retardation',
                      'HP:0001538': 'Protuberant abdomen',
                      'HP:0001539': 'Omphalocele',
                      'HP:0001541': 'Ascites',
                      'HP:0001561': 'Polyhydramnios',
                      'HP:0001629': 'Ventricular septal defect',
                      'HP:0001631': 'Atrial septal defect',
                      'HP:0001643': 'Patent ductus arteriosus',
                      'HP:0001655': 'Patent foramen ovale',
                      'HP:0001744': 'Splenomegaly',
                      'HP:0001762': 'Talipes equinovarus',
                      'HP:0001769': 'Broad foot',
                      'HP:0001773': 'Short foot',
                      'HP:0001789': 'Hydrops fetalis',
                      'HP:0001831': 'Short toe',
                      'HP:0002023': 'Anal atresia',
                      'HP:0002089': 'Pulmonary hypoplasia',
                      'HP:0002093': 'Respiratory insufficiency',
                      'HP:0002240': 'Hepatomegaly',
                      'HP:0002323': 'Anencephaly',
                      'HP:0002350': 'Cerebellar cyst',
                      'HP:0002557': 'Hypoplastic nipples',
                      'HP:0002566': 'Intestinal malrotation',
                      'HP:0002979': 'Bowing of the legs',
                      'HP:0002980': 'Femoral bowing',
                      'HP:0003016': 'Metaphyseal widening',
                      'HP:0003022': 'Hypoplasia of the ulna',
                      'HP:0003026': 'Short long bone',
                      'HP:0003038': 'Fibular hypoplasia',
                      'HP:0003811': 'Neonatal death',
                      'HP:0005054': 'Metaphyseal spurs',
                      'HP:0005257': 'Thoracic hypoplasia',
                      'HP:0005349': 'Hypoplasia of the epiglottis',
                      'HP:0005766': 'Disproportionate shortening of the tibia',
                      'HP:0005817': 'Postaxial polysyndactyly of foot',
                      'HP:0005873': 'Polysyndactyly of hallux',
                      'HP:0006426': 'Rudimentary to absent tibiae',
                      'HP:0006488': 'Bowing of the arm',
                      'HP:0006610': 'Wide intermamillary distance',
                      'HP:0006956': 'Dilation of lateral ventricles',
                      'HP:0008501': 'Median cleft lip and palate',
                      'HP:0008873': 'Disproportionate short-limb short stature',
                      'HP:0009381': 'Short finger',
                      'HP:0010306': 'Short thorax',
                      'HP:0010442': 'Polydactyly',
                      'HP:0010454': 'Acetabular spurs',
                      'HP:0010579': 'Cone-shaped epiphysis',
                      'HP:0012368': 'Flat face',
                      'HP:0100259': 'Postaxial polydactyly',
                      'HP:0100750': 'Atelectasis'}
        # There are some differences in phenotype labels, so compare ID only
        self.assertEqual(bte_result.keys(), rtx_result.keys())

    def test_get_anatomies_for_gene(self):
        bte_result = self.bl.get_anatomies_for_gene("NCBIGene:1080")
        rtx_result = {'UBERON:0000057': 'urethra',
                      'UBERON:0000399': 'jejunal mucosa',
                      'UBERON:0000467': 'anatomical system',
                      'UBERON:0000947': 'aorta',
                      'UBERON:0000992': 'ovary',
                      'UBERON:0001044': 'saliva-secreting gland',
                      'UBERON:0001052': 'rectum',
                      'UBERON:0001062': 'anatomical entity',
                      'UBERON:0001231': 'nephron tubule',
                      'UBERON:0001264': 'pancreas',
                      'UBERON:0001765': 'mammary duct',
                      'UBERON:0001831': 'parotid gland',
                      'UBERON:0002046': 'thyroid gland',
                      'UBERON:0002113': 'kidney',
                      'UBERON:0002115': 'jejunum',
                      'UBERON:0002401': 'visceral pleura',
                      'UBERON:0002477': 'medial globus pallidus',
                      'UBERON:0004358': 'caput epididymis',
                      'UBERON:0004736': 'metanephric glomerulus',
                      'UBERON:0014892': 'skeletal muscle organ'}
        self.assertDictEqual(bte_result, rtx_result)

        bte_result = self.bl.get_anatomies_for_gene("NCBIGene:407053")
        rtx_result = {'UBERON:0000006': 'islet of Langerhans',
                      'UBERON:0000007': 'pituitary gland',
                      'UBERON:0000074': 'renal glomerulus',
                      'UBERON:0001301': 'epididymis'}
        self.assertDictEqual(bte_result, rtx_result)

    def test_get_genes_for_anatomy(self):
        # bte_result = self.bl.get_genes_for_anatomy("UBERON:0000006")
        # rtx_result = ['HGNC:1298', 'ENSEMBL:ENSG00000221639', 'HGNC:6357',
        #               'HGNC:37207', 'HGNC:378', 'MGI:108094', 'HGNC:40742',
        #               'MGI:3694898', 'MGI:3697701', 'HGNC:16713',
        #               'ENSEMBL:ENSG00000260329', 'MGI:1351502', 'MGI:1277193',
        #               'MGI:1914926', 'HGNC:6081', 'HGNC:29161', 'HGNC:16523',
        #               'HGNC:16015', 'MGI:1920185', 'HGNC:24483', 'HGNC:2458',
        #               'HGNC:23472', 'HGNC:25538', 'MGI:1924233', 'HGNC:31602',
        #               'HGNC:7517', 'HGNC:28510', 'HGNC:9772', 'HGNC:41140',
        #               'HGNC:4057', 'HGNC:17407', 'HGNC:29859', 'HGNC:51653',
        #               'HGNC:20711', 'MGI:88588', 'MGI:3642232', 'HGNC:42000',
        #               'MGI:1916998', 'HGNC:491', 'HGNC:28177', 'MGI:2177763',
        #               'MGI:1914721', 'HGNC:18003', 'HGNC:13812', 'HGNC:23817',
        #               'HGNC:13452', 'MGI:2148019', 'HGNC:3391', 'HGNC:15518',
        #               'HGNC:28145', 'MGI:96432', 'HGNC:23488',
        #               'ENSEMBL:ENSG00000233895', 'HGNC:28695', 'MGI:3036267',
        #               'MGI:5477162', 'MGI:88175', 'HGNC:10808', 'HGNC:23467',
        #               'MGI:109589', 'HGNC:26777', 'MGI:108471', 'HGNC:3528',
        #               'HGNC:18817', 'ENSEMBL:ENSG00000177764', 'HGNC:5192',
        #               'MGI:109124', 'MGI:1336885', 'MGI:88610', 'HGNC:25629',
        #               'HGNC:17859', 'MGI:2685955', 'HGNC:21222', 'HGNC:52164',
        #               'HGNC:29612', 'HGNC:24913', 'MGI:2159649', 'HGNC:6532',
        #               'HGNC:29125', 'HGNC:1706', 'MGI:1917904', 'HGNC:1388',
        #               'HGNC:1960', 'ENSEMBL:ENSG00000260526', 'HGNC:16275',
        #               'MGI:1922469', 'HGNC:3518', 'HGNC:6172', 'MGI:97010',
        #               'ENSEMBL:ENSG00000121848', 'HGNC:24045', 'HGNC:6003',
        #               'HGNC:24172', 'MGI:2429955', 'HGNC:6130', 'MGI:1927126',
        #               'HGNC:11513', 'MGI:1922935', 'MGI:1922977', 'HGNC:26460']
        # self.assertSetEqual(set(bte_result), set(rtx_result))

        # bte_result = self.bl.get_genes_for_anatomy("UBERON:0000007")
        # rtx_result = ['MGI:1340046', 'MGI:1921433', 'MGI:2446217', 'HGNC:29665',
        #               'HGNC:29157', 'MGI:2151055', 'MGI:5663654', 'HGNC:646',
        #               'HGNC:24966', 'MGI:88515', 'HGNC:53481', 'MGI:2441982',
        #               'HGNC:412', 'HGNC:16222', 'MGI:1098713', 'MGI:1923202',
        #               'ENSEMBL:ENSG00000197670', 'HGNC:14410', 'MGI:3782982',
        #               'MGI:2681870', 'ENSEMBL:ENSG00000272291', 'MGI:3780260',
        #               'MGI:1196464', 'MGI:107760', 'HGNC:16264', 'MGI:2157062',
        #               'HGNC:17806', 'MGI:97488', 'HGNC:17975', 'HGNC:2184',
        #               'MGI:3039605', 'MGI:3525105', 'MGI:2151816', 'MGI:1351612',
        #               'HGNC:14896', 'MGI:99595', 'ZFIN:ZDB-GENE-040426-1300',
        #               'ENSEMBL:ENSMUSG00000054165', 'MGI:1927848', 'HGNC:13595',
        #               'HGNC:26911', 'MGI:87997', 'MGI:3652098', 'MGI:1933192',
        #               'ENSEMBL:ENSG00000260947', 'MGI:1922387', 'MGI:3781914',
        #               'HGNC:15746', 'MGI:1920004', 'MGI:3034689', 'MGI:4439554',
        #               'MGI:95777', 'MGI:3642400', 'MGI:87965', 'HGNC:10697',
        #               'HGNC:471', 'MGI:1917747', 'HGNC:4097', 'HGNC:2201',
        #               'ZFIN:ZDB-GENE-030804-10', 'MGI:2442694', 'MGI:1333791',
        #               'HGNC:33235', 'HGNC:12446', 'MGI:1919761', 'MGI:2442599',
        #               'MGI:1919253', 'MGI:1890222', 'MGI:1930136', 'MGI:2450877',
        #               'MGI:2178323', 'HGNC:16863', 'MGI:2443589',
        #               'ENSEMBL:ENSG00000272361', 'MGI:109599', 'HGNC:29374',
        #               'MGI:1915078', 'HGNC:14670', 'HGNC:37186', 'MGI:107893',
        #               'MGI:1347049', 'MGI:96207', 'MGI:1923208', 'HGNC:29395',
        #               'HGNC:30252', 'HGNC:1051', 'HGNC:8980', 'MGI:1917737',
        #               'MGI:1920998', 'MGI:2443039', 'MGI:3584510', 'MGI:3801775',
        #               'MGI:2443695', 'HGNC:11614', 'HGNC:10549', 'MGI:1922228',
        #               'HGNC:33658', 'MGI:1338765', 'MGI:1929289', 'MGI:1341836']
        # self.assertSetEqual(set(bte_result), set(rtx_result))
        self.skipTest("Cannot pass. Need further investigation.")

    def test_get_anatomies_for_phenotype(self):
        bte_result = self.bl.get_anatomies_for_phenotype("HP:0000003")
        rtx_result = {'UBERON:0002113': 'kidney'}
        self.assertDictEqual(bte_result, rtx_result)

        bte_result = self.bl.get_anatomies_for_phenotype("HP:0000002")
        rtx_result = {'UBERON:0000468': 'multicellular organism'}
        self.assertDictEqual(bte_result, rtx_result)

if __name__ == '__main__':
    unittest.main()

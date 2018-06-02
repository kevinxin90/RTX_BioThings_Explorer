import unittest
from QueryReactome import QueryReactome


class QueryReactomeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reactome = QueryReactome()

    def test_query_uniprot_id_to_reactome_pathway_ids_desc(self):
        bte_result = self.reactome.query_uniprot_id_to_reactome_pathway_ids_desc("P68871")
        rtx_result = {'R-HSA-112310': 'Neurotransmitter release cycle',
                      'R-HSA-112311': 'Neurotransmitter clearance',
                      'R-HSA-1222352': 'Latent infection of Homo sapiens with Mycobacterium tuberculosis',
                      'R-HSA-1222556': 'ROS, RNS production in phagocytes',
                      'R-HSA-1234174': 'Regulation of Hypoxia-inducible Factor (HIF) by oxygen',
                      'R-HSA-1237044': 'Erythrocytes take up carbon dioxide and release oxygen',
                      'R-HSA-1247673': 'Erythrocytes take up oxygen and release carbon dioxide',
                      'R-HSA-1368071': 'NR1D1 (REV-ERBA) represses gene expression',
                      'R-HSA-1483206': 'Glycerophospholipid biosynthesis',
                      'R-HSA-1483249': 'Inositol phosphate metabolism',
                      'R-HSA-156580': 'Phase II - Conjugation of compounds',
                      'R-HSA-1592230': 'Mitochondrial biogenesis',
                      'R-HSA-1614635': 'Sulfur amino acid metabolism',
                      'R-HSA-163200': 'Respiratory electron transport, ATP synthesis by chemiosmotic coupling, and heat production by uncoupling proteins.',
                      'R-HSA-163841': 'Gamma carboxylation, hypusine formation and arylsulfatase activation',
                      'R-HSA-1650814': 'Collagen biosynthesis and modifying enzymes',
                      'R-HSA-1655829': 'Regulation of cholesterol biosynthesis by SREBP (SREBF)',
                      'R-HSA-174824': 'Plasma lipoprotein assembly, remodeling, and clearance',
                      'R-HSA-189445': 'Metabolism of porphyrins',
                      'R-HSA-191273': 'Cholesterol biosynthesis',
                      'R-HSA-194068': 'Bile acid and bile salt metabolism',
                      'R-HSA-196071': 'Metabolism of steroid hormones',
                      'R-HSA-196791': 'Vitamin D (calciferol) metabolism',
                      'R-HSA-196807': 'Nicotinate metabolism',
                      'R-HSA-196849': 'Metabolism of water-soluble vitamins and cofactors',
                      'R-HSA-202131': 'Metabolism of nitric oxide',
                      'R-HSA-2022090': 'Assembly of collagen fibrils and other multimeric structures',
                      'R-HSA-202733': 'Cell surface interactions at the vascular wall',
                      'R-HSA-2046104': 'alpha-linolenic (omega3) and linoleic (omega6) acid metabolism',
                      'R-HSA-209776': 'Amine-derived hormones',
                      'R-HSA-211945': 'Phase I - Functionalization of compounds',
                      'R-HSA-2142753': 'Arachidonic acid metabolism',
                      'R-HSA-2142789': 'Ubiquinol biosynthesis',
                      'R-HSA-2160456': 'Phenylketonuria',
                      'R-HSA-2173782': 'Binding and Uptake of Ligands by Scavenger Receptors',
                      'R-HSA-2187338': 'Visual phototransduction',
                      'R-HSA-2408522': 'Selenoamino acid metabolism',
                      'R-HSA-3299685': 'Detoxification of Reactive Oxygen Species',
                      'R-HSA-351202': 'Metabolism of polyamines',
                      'R-HSA-381426': 'Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs)',
                      'R-HSA-382556': 'ABC-family proteins mediated transport',
                      'R-HSA-389661': 'Glyoxylate metabolism and glycine degradation',
                      'R-HSA-390918': 'Peroxisomal lipid metabolism',
                      'R-HSA-400206': 'Regulation of lipid metabolism by Peroxisome proliferator-activated receptor alpha (PPARalpha)',
                      'R-HSA-400253': 'Circadian Clock',
                      'R-HSA-418346': 'Platelet homeostasis',
                      'R-HSA-428157': 'Sphingolipid metabolism',
                      'R-HSA-4839726': 'Chromatin organization',
                      'R-HSA-5221030': 'TET1,2,3 and TDG demethylate DNA',
                      'R-HSA-5358346': 'Hedgehog ligand biogenesis',
                      'R-HSA-5362517': 'Signaling by Retinoic Acid',
                      'R-HSA-5362768': "Hh mutants that don't undergo autocatalytic processing are degraded by ERAD",
                      'R-HSA-5423646': 'Aflatoxin activation and detoxification',
                      'R-HSA-5578996': 'Defective CYP27A1 causes Cerebrotendinous xanthomatosis (CTX)',
                      'R-HSA-5579000': 'Defective CYP1B1 causes Glaucoma',
                      'R-HSA-5579004': 'Defective CYP26C1 causes Focal facial dermal dysplasia 4 (FFDD4)',
                      'R-HSA-5579005': 'Defective CYP4F22 causes Ichthyosis, congenital, autosomal recessive 5 (ARCI5)',
                      'R-HSA-5579009': 'Defective CYP11B2 causes Corticosterone methyloxidase 1 deficiency (CMO-1 deficiency)',
                      'R-HSA-5579010': 'Defective CYP24A1 causes Hypercalcemia, infantile (HCAI)',
                      'R-HSA-5579011': 'Defective CYP2U1 causes Spastic paraplegia 56, autosomal recessive (SPG56)',
                      'R-HSA-5579012': 'Defective MAOA causes Brunner syndrome (BRUNS)',
                      'R-HSA-5579013': 'Defective CYP7B1 causes Spastic paraplegia 5A, autosomal recessive (SPG5A) and Congenital bile acid synthesis defect 3 (CBAS3)',
                      'R-HSA-5579014': 'Defective CYP27B1 causes Rickets vitamin D-dependent 1A (VDDR1A)',
                      'R-HSA-5579015': 'Defective CYP26B1 causes Radiohumeral fusions with other skeletal and craniofacial anomalies (RHFCA)',
                      'R-HSA-5579017': 'Defective CYP11B1 causes Adrenal hyperplasia 4 (AH4)',
                      'R-HSA-5579019': 'Defective FMO3 causes Trimethylaminuria (TMAU)',
                      'R-HSA-5579021': 'Defective CYP21A2 causes Adrenal hyperplasia 3 (AH3)',
                      'R-HSA-5579026': 'Defective CYP11A1 causes Adrenal insufficiency, congenital, with 46,XY sex reversal (AICSR)',
                      'R-HSA-5579027': 'Defective CYP2R1 causes Rickets vitamin D-dependent 1B (VDDR1B)',
                      'R-HSA-5579028': 'Defective CYP17A1 causes Adrenal hyperplasia 5 (AH5)',
                      'R-HSA-5579030': 'Defective CYP19A1 causes Aromatase excess syndrome (AEXS)',
                      'R-HSA-5619060': 'Defective CP causes aceruloplasminemia (ACERULOP)',
                      'R-HSA-5625886': 'Activated PKN1 stimulates transcription of AR (androgen receptor) regulated genes KLK2 and KLK3',
                      'R-HSA-5633008': 'TP53 Regulates Transcription of Cell Death Genes',
                      'R-HSA-5662702': 'Melanin biosynthesis',
                      'R-HSA-5668599': 'RHO GTPases Activate NADPH Oxidases',
                      'R-HSA-5679090': 'Defective ABCG8 causes gallbladder disease 4 and sitosterolemia',
                      'R-HSA-5679096': 'Defective ABCG5 causes sitosterolemia',
                      'R-HSA-5682113': 'Defective ABCA1 causes Tangier disease',
                      'R-HSA-5686938': 'Regulation of TLR by endogenous ligand',
                      'R-HSA-6782861': 'Synthesis of wybutosine at G37 of tRNA(Phe)',
                      'R-HSA-6788656': 'Histidine, lysine, phenylalanine, tyrosine, proline and tryptophan catabolism',
                      'R-HSA-6798695': 'Neutrophil degranulation',
                      'R-HSA-6805567': 'Keratinization',
                      'R-HSA-68875': 'Mitotic Prophase',
                      'R-HSA-70895': 'Branched-chain amino acid catabolism',
                      'R-HSA-73942': 'DNA Damage Reversal',
                      'R-HSA-75105': 'Fatty acyl-CoA biosynthesis',
                      'R-HSA-76005': 'Response to elevated platelet cytosolic Ca2+',
                      'R-HSA-8856825': 'Cargo recognition for clathrin-mediated endocytosis',
                      'R-HSA-8856828': 'Clathrin-mediated endocytosis',
                      'R-HSA-8935690': 'Digestion',
                      'R-HSA-8956319': 'Nucleobase catabolism',
                      'R-HSA-8963676': 'Intestinal absorption',
                      'R-HSA-8964572': 'Lipid particle organization',
                      'R-HSA-8979227': 'Triglyceride metabolism',
                      'R-HSA-8981607': 'Intracellular oxygen transport',
                      'R-HSA-9018677': 'Biosynthesis of DHA-derived SPMs',
                      'R-HSA-9018679': 'Biosynthesis of EPA-derived SPMs',
                      'R-HSA-9018683': 'Biosynthesis of DPA-derived SPMs',
                      'R-HSA-9027604': 'Biosynthesis of electrophilic ω-3 PUFA oxo-derivatives',
                      'R-HSA-917937': 'Iron uptake and transport',
                      'R-HSA-975634': 'Retinoid metabolism and transport',
                      'R-HSA-977225': 'Amyloid fiber formation',
                      'R-HSA-983169': 'Class I MHC mediated antigen processing & presentation',
                      'R-HSA-983231': 'Factors involved in megakaryocyte development and platelet production'}
        self.assertDictEqual(bte_result, rtx_result)

    def test_query_reactome_pathway_id_to_uniprot_ids_desc(self):
        bte_result = self.reactome.query_reactome_pathway_id_to_uniprot_ids_desc("R-HSA-2168878")
        rtx_result = {}
        self.assertDictEqual(bte_result, rtx_result)

        bte_result = self.reactome.query_reactome_pathway_id_to_uniprot_ids_desc("R-HSA-5423646")
        rtx_result = {'A6NGU5': 'GGT3P',
                      'O14880': 'MGST3',
                      'O43488': 'AKR7A2',
                      'O95154': 'AKR7A3',
                      'P05177': 'CYP1A2',
                      'P08684': 'CYP3A4',
                      'P10620': 'MGST1',
                      'P16444': 'DPEP1',
                      'P19440': 'GGT1',
                      'P20815': 'CYP3A5',
                      'P36269': 'GGT5',
                      'Q03154': 'ACY1',
                      'Q16696': 'CYP2A13',
                      'Q6P531': 'GGT6',
                      'Q8NHP1': 'AKR7L',
                      'Q96HD9': 'ACY3',
                      'Q99735': 'MGST2',
                      'Q9H4A9': 'DPEP2',
                      'Q9H4B8': 'DPEP3',
                      'Q9UJ14': 'GGT7'}
        self.assertDictEqual(bte_result, rtx_result)

    def test_query_uniprot_id_to_interacting_uniprot_ids_desc(self):
        bte_result = self.reactome.query_uniprot_id_to_interacting_uniprot_ids_desc("P62991")
        rtx_result = {'P31750': 'Akt1',
                      'P53349': 'Map3k1',
                      'P70196': 'Traf6',
                      'Q01705': 'Notch1'}
        self.assertDictEqual(bte_result, rtx_result)

        bte_result = self.reactome.query_uniprot_id_to_interacting_uniprot_ids_desc("P04150")
        rtx_result = {'P00533': 'EGFR',
                      'P06239': 'LCK',
                      'P07900': 'HSP90AA1',
                      'P31749': 'AKT1',
                      'P31948': 'STIP1'}
        self.assertDictEqual(bte_result, rtx_result)


if __name__ == '__main__':
    unittest.main()

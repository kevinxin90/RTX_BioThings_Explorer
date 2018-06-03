import unittest
from numpy.testing import assert_almost_equal
from QueryChembl import QueryChEMBL


class QueryChemblTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chembl = QueryChEMBL()

    def test_get_chembl_ids_for_drug(self):
        bte_result = self.chembl.get_chembl_ids_for_drug("acetaminophen")
        rtx_result = {'CHEMBL112'}
        self.assertSetEqual(bte_result, rtx_result)

        bte_result = self.chembl.get_chembl_ids_for_drug("lovastatin")
        rtx_result = {'CHEMBL503'}
        self.assertSetEqual(bte_result, rtx_result)

    def test_get_target_uniprot_ids_for_chembl_id(self):
        bte_result = self.chembl.get_target_uniprot_ids_for_chembl_id("CHEMBL112")
        rtx_result = {'O14965': 0.11507762987,
                      'O43570': 0.83489320021,
                      'P00915': 0.58779850683,
                      'P00918': 0.75324395458,
                      'P06746': 0.27060403877,
                      'P07550': 0.55051772349,
                      'P08588': 0.51316051544,
                      'P10253': 0.04777717661,
                      'P10636': 0.50837605087,
                      'P13945': 0.3807973039,
                      'P14902': 0.72369037686,
                      'P16473': 0.03583845187,
                      'P43166': 0.23074146691,
                      'P51812': 0.10160386041,
                      'P68400': 0.12196511996,
                      'Q16790': 0.82083804827,
                      'Q92769': 0.04977655439,
                      'Q9NUW8': 0.17706599131,
                      'Q9ULX7': 0.1079090019,
                      'Q9Y468': 0.15028619946}
        self.assertEqual(len(bte_result), len(rtx_result))
        for key, value in bte_result.items():
            assert_almost_equal(rtx_result[key], value, decimal=1)

        bte_result = self.chembl.get_target_uniprot_ids_for_chembl_id("CHEMBL503")
        rtx_result = {'P04035': 1.0,
                      'P04066': 0.00771649434,
                      'P05121': 0.02254928347,
                      'P05129': 0.00364102111,
                      'P08172': 0.7378545703,
                      'P10415': 0.00025222226,
                      'P11229': 0.01304506567,
                      'P17252': 0.00046114296,
                      'P19838': 0.95810776692,
                      'P28074': 0.13827475926,
                      'P35610': 0.05352502034,
                      'P54132': 0.14057925283,
                      'P55212': 0.00045418372,
                      'Q02156': 0.00603731717,
                      'Q13002': 0.00111548102,
                      'Q13285': 0.00121127602,
                      'Q14790': 0.1877639949,
                      'Q15125': 0.00244478854,
                      'Q16665': 0.00415191958,
                      'Q9NY91': 0.0006078251}
        self.assertEqual(len(bte_result), len(rtx_result))
        for key, value in bte_result.items():
            assert_almost_equal(rtx_result[key], value, decimal=1)

    def test_get_target_uniprot_ids_for_drug(self):
        bte_result = self.chembl.get_target_uniprot_ids_for_drug("clothiapine")
        rtx_result = {'P04637': 0.12499267788,
                      'P06746': 0.04246537619,
                      'P08173': 0.18274693348,
                      'P08913': 0.99973447457,
                      'P10635': 0.09162534744,
                      'P11229': 0.16526971365,
                      'P14416': 0.99996980427,
                      'P18089': 0.99638618971,
                      'P18825': 0.97356918354,
                      'P21728': 0.99999999997,
                      'P21917': 0.99500274146,
                      'P21918': 0.9999999824,
                      'P25100': 0.0855003718,
                      'P28223': 0.96867458111,
                      'P28335': 0.98581821496,
                      'P34969': 0.39141293908,
                      'P35367': 0.99996179618,
                      'P35462': 0.11109632984,
                      'P41595': 0.31891025293,
                      'Q9H3N8': 0.83028164473}
        self.assertEqual(len(bte_result), len(rtx_result))
        for key, value in bte_result.items():
            assert_almost_equal(rtx_result[key], value, decimal=1)

        bte_result = self.chembl.get_target_uniprot_ids_for_drug("lovastatin")
        rtx_result = {'P04035': 1.0,
                      'P04066': 0.00771649434,
                      'P05121': 0.02254928347,
                      'P05129': 0.00364102111,
                      'P08172': 0.7378545703,
                      'P10415': 0.00025222226,
                      'P11229': 0.01304506567,
                      'P17252': 0.00046114296,
                      'P19838': 0.95810776692,
                      'P28074': 0.13827475926,
                      'P35610': 0.05352502034,
                      'P54132': 0.14057925283,
                      'P55212': 0.00045418372,
                      'Q02156': 0.00603731717,
                      'Q13002': 0.00111548102,
                      'Q13285': 0.00121127602,
                      'Q14790': 0.1877639949,
                      'Q15125': 0.00244478854,
                      'Q16665': 0.00415191958,
                      'Q9NY91': 0.0006078251}
        self.assertEqual(len(bte_result), len(rtx_result))
        for key, value in bte_result.items():
            assert_almost_equal(rtx_result[key], value, decimal=1)


if __name__ == '__main__':
    unittest.main()

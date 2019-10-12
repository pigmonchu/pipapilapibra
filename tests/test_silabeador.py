import unittest
from pipapilapibra.silabeador import *

class TestSilabeador(unittest.TestCase):

    def test_group_vocalic_monosilabic(self):
        self.assertEqual(gruposVocales('caso'), [(1,'a'), (3, 'o')])
        self.assertEqual(gruposVocales('casal'), [(1,'a'), (3, 'a')])


    def test_diptongos(self):
        self.assertTrue(esDiptongo(0, 'ui'))
        self.assertTrue(esDiptongo(0, 'ai'))
        self.assertTrue(esDiptongo(0, 'ia'))
        self.assertTrue(esDiptongo(0, 'uy'))
        self.assertTrue(esDiptongo(0, 'oy'))

    def test_group_vocalic_diptongo(self):
        self.assertEqual(gruposVocales('queso'), [(1,'ue'), (4, 'o')])
        self.assertEqual(gruposVocales('hoy'), [(1, 'oy')])

    def test_group_vocal_triptongo(self):
        self.assertEqual(gruposVocales('remiau'), [(1, 'e'), (3, 'iau')])
        self.assertEqual(gruposVocales('guay'), [(1, 'uay')])

    def test_consonantes_delante(self):
         self.assertEqual(laConsonante('remiau', 1), 'r')
         self.assertEqual(laConsonante('yo', 1), 'y')
         self.assertEqual(laConsonante('arroz', 3, delante=False), 'z')

    def test_consonantes_delante_False(self):
        self.assertEqual(laConsonante('agua', 0), None)
        self.assertEqual(laConsonante('agua', 3, delante=False), None)
        self.assertEqual(laConsonante('agua', 4, delante=False), None)
        self.assertEqual(laConsonante('agua', -1), None)
        self.assertEqual(laConsonante('', 0, delante=False), None)

    def test_consonante_a_la_izquierda(self):
        self.assertEqual(consonantesDelante('remiau', [(1, 'e'), (3, 'iau')]), [(0, 're'), (2, 'miau')])
        self.assertEqual(consonantesDelante('rastrear', [(1, 'a'), (5, 'e'), (6, 'a')]), [(0, 'ra'), (3, 'tre'), (6, 'a')])
        self.assertEqual(consonantesDelante('rastrejar', [(1, 'a'), (5, 'e'), (7, 'a')]),[(0, 'ra'), (3, 'tre'), (6, 'ja')])

    def test_rellena_derecha(self):
        self.assertEqual(restoHuecos('remiau', [(0, 're'), (2, 'miau')]), [(0, 're'), (2, 'miau')])
        self.assertEqual(restoHuecos('rastrear', [(0, 'ra'), (3, 'tre'), (6, 'a')]), [(0, 'ras'), (3, 'tre'), (6, 'ar')])
        self.assertEqual(restoHuecos('rastrejar', [(0, 'ra'), (3, 'tre'), (6, 'ja')]), [(0, 'ras'), (3, 'tre'), (6, 'jar')])
        self.assertEqual(restoHuecos('rastrejares', [(0, 'ra'), (3, 'tre'), (6, 'ja'), (8, 're')]), [(0, 'ras'), (3, 'tre'), (6, 'ja'), (8, 'res')])

    def test_excepciones(self):
        self.assertEqual(excepciones('inacción', [(0, 'i'), (1, 'nac'), (4, 'ción')]), [(0, 'in'), (2, 'ac'), (4, 'ción')])

    def test_silabeador(self):
        self.assertEqual(silabea('inacción'), ['in', 'ac','ción'])
        self.assertEqual(silabea('rastrejar'), ['ras', 'tre', 'jar'])
        self.assertEqual(silabea('muy'), ['muy'])
        self.assertEqual(silabea('tuyos'), ['tu', 'yos'])

    def test_silabeador_mayusculas(self):
        self.assertEqual(silabea('InacCiÓn'), ['In', 'ac', 'CiÓn'])
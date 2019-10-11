import unittest
from silabeador import *

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
         self.assertTrue(hayConsonante('remiau', 1))
         self.assertTrue(hayConsonante('yo', 1))
         self.assertTrue(hayConsonante('arroz', 3, delante=False))

    def test_consonantes_delante_False(self):
        self.assertFalse(hayConsonante('agua', 0))
        self.assertFalse(hayConsonante('agua', 3, delante=False))
        self.assertFalse(hayConsonante('agua', 4, delante=False))
        self.assertFalse(hayConsonante('agua', -1))
        self.assertFalse(hayConsonante('', 0, delante=False))


    def test_consonante_a_la_izquierda(self):
        self.assertEqual(consonantesDelante('remiau', [(1, 'e'), (3, 'iau')]), [(0, 're'), (2, 'miau')])
        self.assertEqual(consonantesDelante('rastrear', [(1, 'a'), (5, 'e'), (6, 'a')]), [(0, 'ra'), (3, 'tre'), (4, 'a')])

if __name__ == '__main__':
    unittest.main()
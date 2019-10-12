import unittest
from pipapilapibra.pilengua import *

class TestPilengua(unittest.TestCase):

    def test_word(self):
        self.assertEqual(pilengua('mangachapuy'), 'pimanpigapichapipuy')
        self.assertEqual(pilengua('MangAchapuY'), 'piManpigApichapipuY')

    def test_phrase(self):
        self.assertEqual(pilengua('Es una casa muy bonita, Ramón'), 'pies piupina picapisa pimuy pibopinipita, pirrapimón')
        self.assertEqual(pilengua('Esa acción es muy interesante, interactiva y mangachapuy'),'piepisa piacpición pies pimuy piinpitepirepisanpite, piinpitepiracpitipiva piy pimanpigapichapipuy')
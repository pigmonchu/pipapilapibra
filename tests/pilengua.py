import unittest
from app.pilengua import *

class TestPilengua(unittest.TestCase):

    def test_word(self):
        self.assertEqual(pilengua('mangachapuy'), 'pimanpigapichapipuy')
        self.assertEqual(pilengua('MangAchapuY'), 'piManpigApichapipuY')

    def test_phrase(self):
        self.assertEqual(pilengua('Es una casa muy bonita, Ramón'), 'pies piupina picapisa pimuy pibopinipita, pirrapimón')
import unittest

from unit6.review.Exercice3 import strplus


class MyTestCase(unittest.TestCase):
    def test_exercice3(self):
        texto = strplus('algo')
        self.assertEqual('algo', texto)
        texto = texto << ' mas'
        self.assertEqual('algo mas', texto)
        texto = texto - 'as'
        self.assertEqual('algo m', texto)
        self.assertEqual('m ogla', ~texto)


if __name__ == '__main__':
    unittest.main()

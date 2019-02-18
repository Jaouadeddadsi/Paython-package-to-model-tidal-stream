# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from Model_1DV import Model


class TestModel_1DV(unittest.TestCase):

    def setUp(self):
        self.model = Model(500, 2)

    def test_initialization(self):
        self.assertEqual(self.model.grid_size, 500, 'incorrect grid size')
        self.assertEqual(self.model.t_end, 2*24*3600, 'incorrect end time')

    def test_physical_parametre(self):
        self.model.physical_parametre()
        self.assertEqual(self.model.GRAV, 9.81, 'incorrect GRAV')
        self.assertEqual(self.model.FCOR, 1e-4, 'incorrect FCOR')
        self.assertEqual(self.model.KAPPA, 0.4, 'incorrect KAPPA')
        self.assertEqual(self.model.Z0B, 0.0035, 'incorrect Z0B')
        self.assertEqual(self.model.RHO_REF, 1026, 'incorrect RHO_REF')
        self.assertEqual(self.model.CD_AIR, 0.0016, 'incorrect CD_AIR')


if __name__ == '__main__':
    unittest.main()

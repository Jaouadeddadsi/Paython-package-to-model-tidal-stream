from .Generalmodel import CoastalModel
from .Dynamic import estimate_explicite_matrix, estimate_implicite_matrix
import numpy as np
import matplotlib.pyplot as plt


class Model(CoastalModel):

    def __init__(self, grid_size, t_end):
        """Model for solving primitive equation of the ocean in one dimension.

        Attributes:
            grid_size (int) size of the grid
            t_end (float) time to end the simulation in day
        """

        self.grid_size = grid_size
        # Creation of CoastalModel object
        CoastalModel.__init__(self, imax=3, jmax=3, kmax=100)
        # Time parametrisation
        self.t_str = 0  # Start time
        self.t_end = t_end*24*3600  # End time in seconds since t_str
        self.t_out = 0.  # First date of output (in seconds since t_str)
        self.dt_out = 1. * 3600  # Output period in seconds (each hour)
        self.ndtfast = 0  # Number of sub-barotropic time step per 3D time step

    def physical_parametre(self):
        """Function to define the physicals parametres of the model

        Args:
            None

        return:
            None
        """

        self.GRAV = 9.81  # Gravitational constant in m.s-2
        self.FCOR = 1e-4  # Coriolis parameter (2 cos(latitude) Omega) in rd.s-1
        self.KAPPA = 0.4  # Von Karman constant (without units)
        self.Z0B = .0035  # Rugosity in m
        self.RHO_REF = 1026  # kg.m-3  seawater density
        self.RHO_AIR = 1.25  # kg.m-3  air density
        self.CD_AIR = 0.0016  # Drag coefficient
        pass

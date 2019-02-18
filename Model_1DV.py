from Generalmodel import CoastalModel
from Dynamic import estimate_explicite_matrix, estimate_implicite_matrix
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

    def set_parametre(self):
        """Function to define the physicals parametres of the model

        Args:
            None

        return:
            None
        """

        # Physical Parametrisation
        self.GRAV = 9.81  # Gravitational constant in m.s-2
        self.FCOR = 1e-4  # Coriolis parameter (2 cos(latitude) Omega) in rd/s
        self.KAPPA = 0.4  # Von Karman constant (without units)
        self.Z0B = .0035  # Rugosity in m
        self.RHO_REF = 1026  # kg.m-3  seawater density
        self.RHO_AIR = 1.25  # kg.m-3  air density
        self.CD_AIR = 0.0016  # Drag coefficient
        # Numerical parameters
        self.ALP = 0.5  # Implicitation rate for diffusion equation solving
        self.MU_v = 1e-2  # Vertical turbulent viscosity m2.s-1
        self.MU_h = 1.0  # Horizontal turbulent viscosity m2.s-1
        # Boundary conditions : closed everywhere by default
        self.l_obc = {
            'north': False,
            'south': False,
            'west': False,
            'east': False
        }

    def set_variable(self):
        """Function to define variabeles in the Model

        Args:
            None

        return:
            None
        """

        # Set horizontal cell size and define vertical grid
        (ni, nj, nk) = self.estimate_size_grid()
        self.define_Hgrid(self.grid_size)
        self.define_Vgrid(nk)

        # Initialise bathymetry for U, V and T points
        self.init_bathy(ni, nj)

        # Initialise land/sea mask for U, V, T and S points from bathymetry
        self.init_mask(ni, nj, self.l_obc)

        # Define 3D variables
        self.define_var3D(ni, nj, nk)
        self.kz_u[:] = self.MU_v
        self.kz_v[:] = self.MU_v

        # Define temporary variables
        self.v3d_u = np.zeros((nk, ni, nj))
        self.u3d_v = np.zeros((nk, ni, nj))

        # Define atmospheric forcing variables
        self.Pres = np.ones((ni, nj)) * 1013.15
        self.Xstr = np.zeros((ni, nj)) + self.RHO_AIR * self.CD_AIR * 100.
        self.Ystr = np.zeros((ni, nj))

    def __repr__(self):
        """Function to output the characteristics of the simulation

        Args:
            None

        Returns:
            string: characteristics of the simulation

        """

        return "grid size {}, Simulation time {}"\
            .format(self.grid_size, self.t_end)


if __name__ == '__main__':
    M = Model(500, 2)
    M.set_parametre()
    M.set_variable()

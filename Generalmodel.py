import numpy as np
import netCDF4


class CoastalModel:
    """
    Main class describing the model
    """

    def __init__(self, imax, jmax, kmax):
        """
        Define and initialise the first and last point indexes in the three 
        directions (x,y,z) or (east-west, south-north, vertical).
        Inputs :
          imax : last index in the x direction given by the user
          jmax : last index in the y direction given by the user
          kmax : last index in the z direction given by the user
        Outputs :
          self.imin : first index in the x direction
          self.jmin : first index in the y direction
          self.kmin : first index in the z direction
          self.imax : last index in the x direction
          self.jmax : last index in the y direction
          self.kmax : last index in the z direction
        """
        if imax < 3 or jmax < 3:
            raise Exception('2D grid mesh must be composed of 3 by 3 cells')

        self.imin = 0
        self.imax = imax
        self.jmin = 0
        self.jmax = jmax
        self.kmin = 0
        self.kmax = kmax
        
      
        
      
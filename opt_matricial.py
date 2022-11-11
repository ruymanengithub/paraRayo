# -*- coding: utf-8 -*-
"""

ParaRayO:
Matricial Paraxial Optics Program

To-Do:
* Define an optical system from a number of surfaces, distances, n's
* Define rays with a height and angle.
* Transfer rays through system: refractions, translations
* find stops, pupils, nodal points of system
* display results (different program)

R. Azzollini
2022.11.11

           ___(                        )
          (                          _)
         (_                       __))
           ((                _____)
             (_________)----'
                _/  /
               /  _/
             _/  /
            / __/
          _/ /
         /__/
        //
       /'

"""

# IMPORT STUFF
from pdb import set_trace as stop
import numpy as np
# END IMPORT

class Ray(object):
    def __init__(self, u=0., y=0.):
        self.vector = np.array([u,y])


def phi(n1, n2, R):
    """ """
    return (n2-n1)/R

def refraction(ray, phi):
    """ """
    R = np.array([[1., -phi],[0, 1.]])  
    rayP = Ray()
    rayP.vector = np.matmul(R, ray.vector)
    return rayP


def translation(ray, d):
    """ """
    T = np.array([[1., 0.],[d, 1.]])
    rayP = Ray()
    rayP.vector = np.matmul(T, ray.vector)
    return rayP

def ApertureStop():
    """ 
    Aperture Stop is the aperture in the system that limits
    the bundle of light that propagates through the system
    from the axial object point.
    """
    
def EP():
    """ 
    Entrance Pupil is the image of the AperStop in the object space.
    """

def XP():
    """
    eXit Pupil is the the image of the AperStop in the image space.
    """

def MargRay():
    """ 
    Marginal Ray starts at the axial object position, goes through
    edge of the entrance pupil and defines image locations and 
    pupil sizes. Marginal ray height and ray angle are denoted
    y and u.
    
    When marginal ray crosses the axis (y=0), an image is located,
    and the size of the image is given by the CR height in that
    plane.
    
    """
    
def ChiefRay():
    """
    
    Chief Ray starts at the edge of the object, goes through
    the center of the EP, and define image heights and 
    pupil locations. It goes through center of the stop and 
    the center of the exit pupil. Chief ray height and angle
    are denoted ybar and nubar.
    
    Whenever the CR crosses the axis, a pupil or the stop is
    located, and the pupil radius is given by the MR
    height in that plane.
    
    """




def test1():
    """ """
    
    r1 = Ray(u1, y1)
    
    

if __name__ == "__main__":
    
    test1()

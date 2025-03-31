"""
Brownian Motion simulation module.

This module implements a simulation of Brownian motion behavior for a robot
within a square arena, using only Python standard library and numpy.
"""

from .robot import BrownianRobot
from .simulation import BrownianSimulation

__all__ = ['BrownianRobot', 'BrownianSimulation']
#!/usr/bin/env python3
'''Operate the robot's drivetrain.'''

import math

#from ctre import WPI_VictorSRX
import ctre
from wpilib.command import Subsystem

class Agitator(Subsystem):

    def __init__(self, robot):
        """Save the robot object, and assign and save hardware ports
        connected to the drive motors."""
        super().__init__(name = "agitator")
        self.robot = robot

        self.motor = ctre.TalonSRX(11)

    def agitate(self):
        self.motor.set(1.0)

    def calm(self):
        self.motor.set(0.0)

#!/usr/bin/env python3

import math

import wpilib
from ctre import WPI_VictorSPX
from wpilib.command import Subsystem

class Alligator(Subsystem):
    '''Operate the drivetrain.'''

    def __init__(self, robot):
        '''Save the robot object, and assign and save hardware ports
        connected to the drive motors.'''
        super().__init__(name = "intake")
        self.robot = robot

        self.motor = WPI_VictorSPX(11)

    def agitate(self):
        self.motor.set(1.0)

    def calm(self):
        self.motor.set(0.0)
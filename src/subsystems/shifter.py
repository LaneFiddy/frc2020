#!/usr/bin/env python3
'''Operate the robot's drivetrain.'''

import wpilib
from wpilib.command import Subsystem
from wpilib import DoubleSolenoid

class Shifter(Subsystem):

    def __init__(self, robot):
        """Save the robot object, and assign and save hardware ports
        connected to the drive motors."""
        super().__init__(name = "shifter")
        self.robot = robot

        self.piston = wpilib.DoubleSolenoid(0,3,2)

    def shiftUp(self):
        self.piston.set(DoubleSolenoid.Value.kForward)

    def shiftDown(self):
        self.piston.set(DoubleSolenoid.Value.kReverse)
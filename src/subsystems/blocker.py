#!/usr/bin/env python3
'''Operate the robot's drivetrain.'''

import wpilib
from wpilib.command import Subsystem
from wpilib import DoubleSolenoid

class Blocker(Subsystem):
    """Operate the drivetrain."""

    def __init__(self, robot):
        """Save the robot object, and assign and save hardware ports
        connected to the drive motors."""
        super().__init__(name = "blocker")
        self.robot = robot

        self.piston = wpilib.DoubleSolenoid(0,6,7)

    def block(self):
        self.piston.set(DoubleSolenoid.Value.kForward)
        print("blocking")

    def release(self):
        self.piston.set(DoubleSolenoid.Value.kReverse)
        print("releasing")
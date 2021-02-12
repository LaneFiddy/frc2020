#!/usr/bin/env python3
'''Operate the robot's drivetrain.'''

import math

import wpilib, rev
from wpilib.command import Subsystem

class Shooter(Subsystem):
    """Operate the drivetrain."""

    def __init__(self, robot):
        """Save the robot object, and assign and save hardware ports
        connected to the drive motors."""
        super().__init__(name = "shooter")
        self.robot = robot

        self.top = rev.CANSparkMax(9, rev.CANSparkMax.MotorType.kBrushless)
        self.bottom = rev.CANSparkMax(10, rev.CANSparkMax.MotorType.kBrushless)

    def shoot(self):
        print("shooting")
        self.top.set(.6)
        self.bottom.set(1.0)

    def stopShooting(self):
        self.top.set(0)
        self.bottom.set(0)

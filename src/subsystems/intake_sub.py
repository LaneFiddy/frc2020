#!/usr/bin/env python3

import math

import wpilib
from ctre import WPI_TalonSRX
from wpilib.command import Subsystem

class Intake_Sub(Subsystem):
    """Operate the drivetrain."""

    def __init__(self, robot):
        """Save the robot object, and assign and save hardware ports
        connected to the drive motors."""
        super().__init__(name = "intake")
        self.robot = robot

        self.motor = ctre.WPI_TalonSRX(7)

    def intake(self):
        self.motor.set(1.0)

    def stop(self):
        self.motor.set(0)

    def eject(self):
        self.motor.set(-.5)
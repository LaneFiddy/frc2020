#!/usr/bin/env python3

import math

import wpilib, rev
from wpilib.command import Subsystem

class Intake_Sub(Subsystem):
    """Operate the drivetrain."""

    def __init__(self, robot):
        """Save the robot object, and assign and save hardware ports
        connected to the drive motors."""
        super().__init__(name = "shooter")
        self.robot = robot

        self.motor = rev.CANSparkMax(7, rev.CANSparkMax.MotorType.kBrushless)

    def intake(self):
        self.motor.set(.6)

    def stop(self):
        self.motor.set(0)

    def eject(self):
        self.motor.set(-.5)
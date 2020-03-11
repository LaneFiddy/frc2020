#!/usr/bin/env python3

from wpilib.command import Subsystem
from wpilib import Encoder
from ctre import WPI_VictorSPX

class Climbmotors(Subsystem):
    """Raise and lower the robot's arm."""
    def __init__(self, robot):
        """Assign ports and save them for use in the move and stop methods."""
        super().__init__()

        self.motor1 = WPI_VictorSPX(5)
        self.motor2 = WPI_VictorSPX(6)

    def climb(self, value):
        self.motor2.follow(self.motor1)
        self.motor1.set(value)


    def stop(self):
        self.motor2.follow(self.motor1)
        self.motor1.set(0.0)
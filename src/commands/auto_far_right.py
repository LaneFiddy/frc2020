#!/usr/bin/env python3
'''Drive differentially with an Xbox controller.'''

from wpilib.command import CommandGroup
from .shoot import Shoot
from .drive_forward import DriveForward
from wpilib.command import WaitCommand

class AutoFarRight(CommandGroup):
    def __init__(self, robot):
        super().__init__()
        self.robot = robotn

        self.addSequential(DriveForward(robot), 0.4)
        self.addSequential(Shoot(robot), 2.0)
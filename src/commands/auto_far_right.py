#!/usr/bin/env python3

from wpilib.command import CommandGroup
from wpilib.command import WaitCommand
from .shoot import Shoot
from .drive_reverse import DriveReverse

class AutoFarRight(CommandGroup):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.addSequential(DriveReverse(robot), 0.4)
        self.addSequential(Shoot(robot), 2.0)
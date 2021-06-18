#!/usr/bin/env python3

from wpilib.command import CommandGroup
from wpilib.command import WaitCommand
from subsystems.shooter import Shooter
from .unblock import Unblock
from .drive_reverse import DriveReverse

class AutoBackupShoot(CommandGroup):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.addSequential(DriveReverse(robot), 2.0)
        self.addSequential(Shoot(robot), 2.0)


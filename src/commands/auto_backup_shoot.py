#!/usr/bin/env python3
'''Drive differentially with an Xbox controller.'''

from wpilib.command import CommandGroup
from .shoot import Shoot
from .unblock import Unblock
from .drive_forward import DriveReverse
from wpilib.command import WaitCommand

class AutoBackupShoot(CommandGroup):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.addSequential(DriveForward(robot), 2.0)
        self.addSequential(Shoot(robot), 2.0)

        #self.addSequential(DriveReverse(robot), 1.0)
        #self.addSequential(Unblock(robot), 3.0)
        #self.addParallel(Shoot(robot), 3.0)

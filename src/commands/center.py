#!/usr/bin/env python3

from wpilib.command import CommandGroup
from wpilib.command import WaitCommand
from .shoot import Shoot
from .drive_forward import DriveForward
from .drive_reverse import DriveReverse
from .releaseshoot import ReleaseShoot
from .block import Block
from .unblock import Unblock

class Center(CommandGroup):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.addParallel(Shoot(robot), 6.0)
        self.addSequential(WaitCommand(2.0))
        self.addSequential(Unblock(robot), 6.5)
        self.addSequential(DriveReverse(robot), 3.0)
        self.addSequential(Block(robot))

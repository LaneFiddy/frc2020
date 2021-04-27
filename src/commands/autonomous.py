#!/usr/bin/env python3
'''Drive differentially with an Xbox controller.'''

from wpilib.command import CommandGroup
from .shoot import Shoot
from .stopshooting import StopShooting
from .block import Block
from .unblock import Unblock
from wpilib.command import WaitCommand

class ReleaseShoot(CommandGroup):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.addSequential(Shoot(robot), 2.0)
        self.addSequential(Unblock(robot), 10.0)
        self.addSequential(StopShooting(robot))
        self.addParallel(Block(robot))
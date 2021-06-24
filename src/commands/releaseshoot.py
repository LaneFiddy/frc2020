#!/usr/bin/env python3
'''Drive differentially with an Xbox controller.'''

from wpilib.command import CommandGroup
from .shoot import Shoot
from .stopshooting import StopShooting
from .block import Block
from .unblock import Unblock
from wpilib.command import WaitCommand

class ReleaseShoot(CommandGroup):
    #TODO:The drive team would like this timing to change. Ask them for more info.
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.addParallel(Shoot(robot), 6.0)
        self.addParallel(WaitCommand(2.0))
        self.addSequential(Unblock(robot), 10.0)
        #self.addSequential(StopShooting(robot), 1.0)
        self.addSequential(Block(robot), 1.0)

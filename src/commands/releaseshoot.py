#!/usr/bin/env python3
'''Drive differentially with an Xbox controller.'''

from wpilib.command import CommandGroup
from commands.block import Block
from commands.shoot import Shoot
from commands.stopshooting import StopShooting
from commands.unblock import Unblock
from wpilib.command import WaitCommand

class ReleaseShoot(CommandGroup):
    def __init(self, robot):
        super().__init__()
        self.addSequential(Shoot(robot))
        self.addSequential(WaitCommand(timeout=0.3))
        self.addSequential(Unblock(robot))
        self.addSequential(WaitCommand(timeout=5))
        #TODO: figure out how long the shooter needs to run in order to empty
        self.addSequential(StopShooting(robot))
        self.addParallel(Block(robot))
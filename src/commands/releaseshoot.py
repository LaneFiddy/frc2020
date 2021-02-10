#!/usr/bin/env python3
'''Drive differentially with an Xbox controller.'''

from wpilib.command import CommandGroup
import commands
from wpilib.command import WaitCommand

class ReleaseShoot(CommandGroup):
    def __init(self, robot):
        super().__init__()

        self.addSequential(commands.Shoot(robot))
        self.addSequential(WaitCommand(timeout=0.3))
        self.addSequential(commands.Unblock(robot))
        self.addSequential(WaitCommand(timeout=5))
        #TODO: figure out how long the shooter needs to run in order to empty
        self.addSequential(commands.StopShooting(robot))
        self.addParallel(commands.Block(robot))

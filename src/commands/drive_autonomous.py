#!/usr/bin/env python3
'''Drive differentially with an Xbox controller.'''

from wpilib.command import CommandGroup
from .drive_forward import DriveForward
from wpilib.command import WaitCommand

class DriveAutonomous(CommandGroup):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot

        self.addSequential(DriveForward(robot, 10, 0.2))
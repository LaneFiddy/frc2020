#!/usr/bin/env python3
'''Drive differentially with an Xbox controller.'''

from wpilib.command import Command

class Agitate(Command):

    def __init__(self, robot):
        '''Save the robot object and pull in the drivetrain subsystem.'''
        super().__init__()

        self.robot = robot
        self.requires(self.robot.agitator)

    def initialize(self):
        """Called just before this Command runs the first time"""
        print ("shoot initialize")

    def execute(self):
        """Called repeatedly when this Command is scheduled to run."""
        self.robot.agitator.agitate()
        print ("shooot execute")

    def isFinished(self):
        """Make this return true when this Command no longer needs to
        run execute()"""
        return False  # Runs until interrupted

    def end(self):
        """Called once after isFinished returns true"""
        self.robot.agitator.calm()

    def interrupted(self):
        """Called when another command which requires one or more of
        the same subsystems is scheduled to run"""
        self.end()

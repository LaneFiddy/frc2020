#!/usr/bin/env python3

from wpilib.command import Command

class Intake_Com(Command):
    '''Drive differentially with an Xbox controller.'''
    def __init__(self, robot):
        '''Save the robot object and pull in the drivetrain subsystem.'''
        super().__init__()

        self.robot = robot
        self.requires(self.robot.intake_sub)

    def initialize(self):
        """Called just before this Command runs the first time"""

    def execute(self):
        """Called repeatedly when this Command is scheduled to run."""
        print("in execute")
        self.robot.intake_sub.intake()

    def isFinished(self):
        """Make this return true when this Command no longer needs to
        run execute()"""
        return False  # Runs until interrupted

    def end(self):
        """Called once after isFinished returns true"""
        self.robot.intake_sub.stop()

    def interrupted(self):
        """Called when another command which requires one or more of
        the same subsystems is scheduled to run"""
        self.end()

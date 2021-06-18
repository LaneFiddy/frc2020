#!/usr/bin/python3
'''robot.py: The "main" line of the code.'''

import math
import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler
from subsystems.drivetrain import DriveTrain
from subsystems.shooter import Shooter
from subsystems.blocker import Blocker
from subsystems.intake_sub import Intake_Sub
from subsystems.shifter import Shifter
from subsystems.climbmotors import Climbmotors
from subsystems.climbpistons import Climbpistons

from subsystems.agitator import Agitator

from commands.auto_backup_shoot import AutoBackupShoot
from commands.auto_far_left import AutoFarLeft
from commands.auto_far_right import AutoFarRight
from commands.auto_shoot import AutoShoot

from oi import OI

class MyRobot(CommandBasedRobot):
    '''Primary class, the Periodic methods in which are called
    repeatedly by the RoboRIO system service.'''

    def robotInit(self):
        '''Initialize all subsystems.'''
        self.drivetrain = DriveTrain(self)
        self.shooter = Shooter(self)
        self.intake_sub = Intake_Sub(self)
        self.shifter = Shifter(self)
        self.blocker = Blocker(self)
        self.climbmotors = Climbmotors(self)
        self.climbpistons = Climbpistons(self)
        self.agitator = Agitator(self)

        self.autoChooser = wpilib.SendableChooser()
        self.autoChooser.setDefaultOption("Default", AutoBackupShoot)

        # The "front" of the robot (which end is facing forward)
        self.front = -1

        self.oi = OI(self)

    def disabledInit(self):
        '''Initialize systems when entering Disabled Mode.'''

    def disabledPeriodic(self):
        '''Called approximately every 20ms while in Disabled Mode.'''
        return super().disabledPeriodic()

    def autonomousInit(self):
        self.autonomousCommand = self.autoChooser.getSelected()
        self.autonomousCommand.start()
        '''Initialize systems when entering Autonomous Mode.'''

    def autonomousPeriodic(self):
        '''Called approximately every 20ms while in Autonomous Mode.'''
        Scheduler.getInstance().run()

    def teleopInit(self):
        '''Initialize systems when entering Teleoperated Mode.'''

    def teleopPeriodic(self):
        '''Called approximately every 20ms while in Teleoperated Mode.'''
        Scheduler.getInstance().run()

    def testInit(self):
        '''Initialize systems when entering Test Mode.'''

    def testPeriodic(self):
        '''Called approximately every 20ms while in Test Mode.'''
        Scheduler.getInstance().run()

if __name__ == "__main__":
    '''Kick off the robot code.'''
    wpilib.run(MyRobot)

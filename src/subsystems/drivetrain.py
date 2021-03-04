#!/usr/bin/env python3
'''Operate the robot's drivetrain.'''

import math

import wpilib, rev
from wpilib.command import Subsystem
from wpilib.drive import DifferentialDrive

class DriveTrain(Subsystem):
    """Operate the drivetrain."""

    def __init__(self, robot):
        """Save the robot object, and assign and save hardware ports
        connected to the drive motors."""
        super().__init__(name = "drivetrain")
        self.robot = robot

        # The digital gyro plugged into the SPI port on RoboRIO
        self.gyro = wpilib.ADXRS450_Gyro()

        # Motors used for driving
        self.left = rev.CANSparkMax(1, rev.CANSparkMax.MotorType.kBrushless)
        self.leftB = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushless)
        self.right = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushless)
        self.rightB = rev.CANSparkMax(4, rev.CANSparkMax.MotorType.kBrushless)

        # TODO: switch to DifferentialDrive is the main object that deals with driving
        self.drive = DifferentialDrive(self.left, self.right)

        #TODO: These probably will not be the actual ports used
        self.left_encoder = wpilib.Encoder(2, 3)
        self.right_encoder = wpilib.Encoder(4, 5)

        # Encoders may measure differently in the real world and in
        # simulation. In this example the robot moves 0.042 barleycorns
        # per tick in the real world, but the simulated encoders
        # simulate 360 tick encoders. This if statement allows for the
        # real robot to handle this difference in devices.
        # TODO: Measure our encoder's distance per pulse
        if robot.isReal():
            self.left_encoder.setDistancePerPulse(0.042)
            self.right_encoder.setDistancePerPulse(0.042)
        else:
            # Circumference in ft = 4in/12(in/ft)*PI
            self.left_encoder.setDistancePerPulse((4.0 / 12.0 * math.pi) / 360.0)
            self.right_encoder.setDistancePerPulse((4.0 / 12.0 * math.pi) / 360.0)

    def driveManual(self, xboxcontroller):
        #self.leftB.follow(self.left, followerType=0)
        #self.rightB.follow(self.right, followerType=0)
        #TODO: I'm not sure if these followers should be on or not. Let's find that out.
        self.drive.arcadeDrive(-xboxcontroller.getY(wpilib.interfaces._interfaces.GenericHID.Hand.kLeftHand), xboxcontroller.getX(wpilib.interfaces._interfaces.GenericHID.Hand.kLeftHand))

    def driveForward(self, dist):
            self.drive.tankDrive(.5,.5)

    def stopDriving(self):
        self.drive.tankDrive(0,0)

    def getHeading(self):
        """Get the robot's heading in degrees"""
        return self.gyro.getAngle()

    def reset(self):
        """Reset the robots sensors to the zero states."""
        self.gyro.reset()
        self.left_encoder.reset()
        self.right_encoder.reset()

    def getDistance(self):
        """Get the current distance driven.
        :returns: The distance driven (average of left and right encoders)"""
        return (
            self.left_encoder.getDistance().__init__()
        ) / 2.0

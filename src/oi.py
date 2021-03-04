#!/usr/bin/python3
'''Operator Interface - one class: OI.
This is where the rubber meets the road: make the Xbox controller
do what we want it to do.
'''
from commands.toggle_camera import ToggleCamera
from commands.drive_with_xbox import DifferentialDriveWithXbox
from commands.invert_front import InvertFront
from commands.releaseshoot import ReleaseShoot
from commands.cuntake import Cuntake
from commands.alligate import Alligate
from commands.shoot import Shoot
from commands.block import Block
from commands.intake_com import Intake_Com
from commands.shiftup import ShiftUp
from commands.shiftdown import ShiftDown
from commands.climbwithtriggers import Climbwithtriggers
from commands.extendclimber import Extendclimber
import wpilib
#import wpilib.interfaces._interfaces.GenericHID
from wpilib.buttons import JoystickButton
from wpilib import XboxController
from thresholds import TriggerButton
from thresholds import StickButton

class OI:
    '''Operator Interface - all button assignments and other human interface elements
    '''

    def __init__(self, robot):
        '''The Constructor - assign Xbox controller buttons to specific Commands.
        '''

        print("In OI:__init__")

        robot.xbox0 = wpilib.XboxController(0)
        robot.xbox1 = wpilib.XboxController(1)

        stickbutton = StickButton(robot.xbox0, .1)
        shoot = JoystickButton(robot.xbox0, XboxController.Button.kA)
        alligate = JoystickButton(robot.xbox0, XboxController.Button.kA)
        block = JoystickButton(robot.xbox0, XboxController.Button.kY)
        intake = JoystickButton(robot.xbox0, XboxController.Button.kX)
        shiftup = JoystickButton(robot.xbox0, XboxController.Button.kBumperRight)
        shiftdown = JoystickButton(robot.xbox0, XboxController.Button.kBumperLeft)
        triggerbutton = TriggerButton(robot.xbox1, .1)
        extendclimber = JoystickButton(robot.xbox1, XboxController.Button.kA)
       
        #releaseshoot = JoystickButton(robot.xbox0, XboxController.Button.kA)
        eject = JoystickButton(robot.xbox0, XboxController.Button.kB)


        togglecamera = JoystickButton(robot.xbox0, XboxController.Button.kStart)
        togglecamera.whenPressed(ToggleCamera(robot))
        stickbutton.whenPressed(DifferentialDriveWithXbox(robot))
        shoot.whileHeld(Shoot(robot))
        alligate.whileHeld(Alligate(robot))
        block.toggleWhenPressed(Block(robot))
        intake.whileHeld(Intake_Com(robot))
        shiftup.whenPressed(ShiftUp(robot))
        shiftdown.whenPressed(ShiftDown(robot))
        triggerbutton.whenPressed(Climbwithtriggers(robot))
        extendclimber.toggleWhenPressed(Extendclimber(robot))

        #releaseshoot.whileHeld(ReleaseShoot(robot))
        eject.whileHeld(Cuntake(robot))
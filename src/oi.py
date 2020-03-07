#!/usr/bin/python3
'''Operator Interface - one class: OI.
This is where the rubber meets the road: make the Xbox controller
do what we want it to do.
'''
from commands.toggle_camera import ToggleCamera
from commands.differentialdrive_with_xbox import DifferentialDriveWithXbox
from commands.invert_front import InvertFront
from commands.shoot import Shoot
from commands.block import Block
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
        block = JoystickButton(robot.xbox0, XboxController.Button.kY)

        togglecamera = JoystickButton(robot.xbox0, XboxController.Button.kStart)
        togglecamera.whenPressed(ToggleCamera(robot))
        stickbutton.whenPressed(DifferentialDriveWithXbox(robot))
        shoot.whileHeld(Shoot(robot))
        block.toggleWhenPressed(Block(robot))
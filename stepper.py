# import RPi.GPIO as GPIO
import time
import os
import sys


class Stepper:
	def __init__(self):
		#Set GPIO pin values
		self.position = 0
		self.run = False
		self.setPosition()
		return

	def getCard(self):
		#We assume here the degree value to get a card from the stack
		self.position = -45
		self.setPosition()
		return

	def finishCard(self):
		self.position = 75
		self.setPosition()
	
	def setPosition(self):
		#uses self.position
		return

	def close(self):
		return
		#Cleanup GPIO


from stepper import Stepper
from camera import Camera
from writer import Writer
from ocr import OCR


class Service:
	def __init__(self):
		#Set GPIO pin values
		self.camera = Camera()
		self.stepper = Stepper()
		self.writer = Writer()
		self.ocr = OCR()
		self.run = False
		return

	def start():
		self.run = True
		self.run()

	def run(self):
		self.stepper.getCard()
		path = self.camera.takePhoto()
		data = self.ocr.ocrImage(path)
		self.writer.writeToFile(data)
		self.stepper.finishCard()
		self.run() #run again



	
	def setPosition(self, position):
		self.position = position
		return

def close(self):
	return
	#Cleanup GPIO
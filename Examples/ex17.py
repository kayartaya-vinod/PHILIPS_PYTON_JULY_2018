class Camera(object):
	def __init__(self, **kwargs):
		print('Camera instance created!')

	def take_picture(self):
		pass

class Radio(object):
	def __init__(self, **kwargs):
		print('Radio instance created!')
	
	def tune_station(self):
		print('tuning station from Radio')

class Phone(object):
	def __init__(self, **kwargs):
		print('Phone instance created!')

	def tune_station(self):
		print('tuning station from Phone')

	def dial_number(self):
		pass

class Smartphone(Camera, Radio, Phone):
	def __init__(self, **kwargs):
		# super().__init__(**kwargs)
		Camera.__init__(self, **kwargs)
		Radio.__init__(self, **kwargs)
		Phone.__init__(self, **kwargs)
		print('Smartphone instance created!')


def main():
	sp1 = Smartphone()
	sp1.take_picture()
	sp1.dial_number()
	sp1.tune_station()

if __name__ == '__main__':
	main()
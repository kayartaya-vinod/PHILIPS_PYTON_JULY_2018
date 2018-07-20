import setuptools

setuptools.setup(
	name="myutils",
	version="1.0.0",
	license="MIT",
	packages=["myutils"],
	package_dir={"myutils": "./myutils"},
	author="Vinod",
	author_email="vinod@vinod.co",
	url="https://vinod.co",
	description='''This is a example package containing a single module:

generators

The module contains two functions:

1. factorial_generator
2. fibonacci_generator

	'''
	)
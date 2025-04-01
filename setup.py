from setuptools import setup

setup(
	name="insyst", 
	version="0.1",
	packages=['insyst'],
	install_requires=['iniconfig==2.1.0',
		'packaging==24.2',
		'pluggy==1.5.0',
		'prompt_toolkit==3.0.50',
		'pyfiglet==1.0.2',
		'pytest==8.3.5',
		'wcwidth==0.2.13'],
	author="alxpx",
	author_email="alxpx@outlook.com",
	description="Displays information ahout the current system.",
	long_description=open("README.md").read(),
	url="https://github.com/alxpxx/insyst",
	license='GNU',
)

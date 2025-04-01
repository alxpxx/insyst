from setuptools import setup, find_packages

setup(
	name="insyst", 
	version="0.1.0"
	packages=find_packages(),
	install_requires=[],
	author="alxpx"
	author_email="alxpx@outlook.com"
	description="Displays information ahout the current system."
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	url="https://github.com/alxpxx/insyst",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: Linux",
	],
	python_requires=">=3.6",
)

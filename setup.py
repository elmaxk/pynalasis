from setuptools import setup, find_packages

setup(
	name='data_analysis',
	version='0.01',
	url='https://github.com/elmaxk/pynalasis',
	license='GPL-3.0',
	author='elmaxk',
	packages=find_packages(),
	entry_points={},
	extras_require={'dev': ['flake8',]},
	)

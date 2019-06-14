from os.path import abspath, dirname, join
from setuptools import setup

# Read the README markdown data from README.md
with open(abspath(join(dirname(__file__), 'README.md')), 'rb') as readmeFile:
	__readme__ = readmeFile.read().decode('utf-8')

setup(
	name='kubernetes-utils',
	version='0.0.2',
	description='Utilities for interacting with the Kubernetes client API',
	long_description=__readme__,
	long_description_content_type='text/markdown',
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
	],
	keywords='kubernetes',
	url='http://github.com/deepdrive/kubernetes-utils',
	author='Deepdrive',
	author_email='craig@deepdrive.io',
	license='MIT',
	packages=['kubernetes_utils'],
	zip_safe=True,
	python_requires = '>=3.5',
	install_requires = [
		'google-auth>=1.6.3',
		'google-cloud-container>=0.2.1',
		'kubernetes>=9.0.0',
		'setuptools>=38.6.0',
		'twine>=1.11.0',
		'wheel>=0.31.0'
	]
)

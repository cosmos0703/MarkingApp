from setuptools import setup

setup(name='marking_app_python',
      version='0.1.0',
      packages=['marking_app_python'],
      entry_points={
          'console_scripts': [
              'marking_app_python = marking_app_python.__main__:main'
          ]})


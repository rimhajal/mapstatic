from setuptools import setup
from mapstatic import __version__ as current_version

setup(
  name='mapstatic',
  version=current_version,
  description='Visualization of the Electricity Consumption and its Prediction',
  url='http://github.com/rimhajal/mapstatic.git',
  author='Thiziri Abchiche ; Rim Alhajal ; Maryem El Yamani ; Lilou Zulewski',
  author_email='lilou_zulewski01@etu.umontpellier.fr',
  license='MIT',
  packages=['mapstatic', 'mapstatic.visualization', 'mapstatic.prediction'],
  zip_safe=False
)

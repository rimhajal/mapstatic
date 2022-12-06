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
  packages=['mapstatic','mapstatic.prediction', 'mapstatic.visualization', 'mapstatic.visualization.geodata', 'mapstatic.visualization.io', 'mapstatic.visualization.vis'],
  zip_safe=False
)

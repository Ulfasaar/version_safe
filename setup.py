from setuptools import setup, find_packages
 
setup(name='version_safe',
      version='0.1-alpha',
      # url='https://github.com/Ulfasaar/cache',
      license='MIT',
      author='Ryan Weyers',
      author_email='weyers.ryan@gmail.com',
      description='A library that makes sharing code across python versions easier',
      # long_description=open('../README.md').read(),
      packages=['.'],
      zip_safe=True)
import setuptools

setuptools.setup(name='pyCCDA',
      version='0.0.1',
      description='CCDA Parser',
      url='https://github.com/MemoirHealth/ccda-parser',
      author='Mansoor Alam',
      author_email='me@mansooralam.com',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=["bluebutton"],
      zip_safe=False)

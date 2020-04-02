from setuptools import setup

setup(name='mgsolver',
      version='0.0.1',
      packages=['mgsolver/ball_sort_puzzle', 'mgsolver/nonogram', 'mgsolver/sudoku'],
      description='Collection of mini game solvers.',
      keywords="mgsolver mini game solver",
      author='Roman Stražanec',
      author_email='roman.strazanec007@gmail.com',
      license='MIT',
      url='https://github.com/romanstrazanec/mgsolver',
      download_url='https://github.com/romanstrazanec/mgsolver/releases/tag/v0.0.1',
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3.8",
          "Topic :: Other/Nonlisted Topic"
      ]
      )

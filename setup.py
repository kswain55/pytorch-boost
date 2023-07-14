from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'pytorch-boost',
  packages = find_packages(),
  version = '0.0.1',
  license='MIT',
  description = 'Deep learning optimization library for PyTorch',
  author = 'minyoung huh, kswain',
  author_email = 'minhuh@mit.edu, kswain@mit.edu',
  url = 'https://github.com/kswain55/pytorch-boost',
  long_description=long_description,
  long_description_content_type = 'text/markdown',
  keywords = [
    'artificial intelligence'
  ],
  install_requires=[
    'torch>=2.0'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10',
  ],
)

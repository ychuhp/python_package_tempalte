import re
from setuptools import find_packages
from setuptools import setup


def find_version(path):
  with open(path, 'r', encoding='utf-8') as stream:
    return re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        stream.read(),
        re.M,
    ).group(1)


def read_long_description(path):
  with open(path, 'r', encoding='utf-8') as stream:
    return stream.read()


# @see https://python-packaging.readthedocs.io/en/latest/index.html  # noqa
# @see https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords  # noqa
# @see https://packaging.python.org/guides/packaging-namespace-packages/#native-namespace-packages  # noqa
setup(
    name='package',
    version=find_version('package/__init__.py'),
    author='Yechan Hong',
    author_email='ychuh@pharmcaad.com',
    url='none',
    license='MIT',
    description='Package',
    long_description=read_long_description('README.md'),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
      'Environment :: GPU :: NVIDIA CUDA :: 10.2',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6.9',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords=[''],
    zip_safe=False,
    python_requires='>=3.6.9',
    install_requires=[
      # LIST THE DEPENDENCIES OF YOUR PACKAGE
      # FOR INSTANCE,
      # 'numpy>=1.19.2,
      'torch>=1.0',
      'numpy',
      'pandas',
      'scikit-learn',
      'scipy',
      'tqdm',
      #'tensorboard',
      'flake8',
      'pre-commit',
    ],
    entry_points={
      'console_scripts': [
        'package-train = package.train:main',
      ]
    },
    # test_suite='nose.collector',
    # tests_require=['nose', 'nose-cover3'],
)

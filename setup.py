from setuptools import setup, find_packages

setup(
    name='win10toast-click',
    version='0.1.2-custom',
    description='Custom fork of win10toast-click with modifications',
    author='Polsi_Hacker',
    url='https://github.com/PolskiHacker/win10_toast_changed.git',
    packages=find_packages(),
    install_requires=[
        'pypiwin32',
        'setuptools'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)
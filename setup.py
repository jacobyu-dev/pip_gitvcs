from setuptools import setup

setup(
    name='test-pkg',
    version='0.0.2',
    description='jk pip install test',
    url='https://github.com/jacobyu-dev/pip_gitvcs.git',
    author='jacob yu',
    author_email='rdx1696@gmail.com',
    license='ypol',
    packages=['test_pkg'],
    zip_safe=False,
    install_requires=[
        'numpy==1.18.3'
    ]
)
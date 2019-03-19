from setuptools import setup, find_packages

setup(
    name='piethorn',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Some of the algorithms using recursion as well as sorting algorithms',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<smtolo>/<piethorn>',
    author='<Sihle Mtolo>',
    author_email='<mr.sihle.mtolo@gmail.com>'
)
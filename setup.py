from setuptools import setup

setup(
        name='pydemo',
        version='1.0',
        description='Automates a python coding demo',
        author='justin dane vrana',
        author_email='justin.vrana@gmail.com',
        url='',
        py_modules='run_demo',
        entry_points={
            'console_scripts': [
                'pydemo = run_demo:main'
            ],
        }
)
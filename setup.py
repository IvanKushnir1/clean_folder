from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'numpy'
    ],
    description='Clean_folder',
    author='Ivan',
    entry_points={
        'console_scripts': ['clean-folder = clean_folder.clean:main']
    }
)
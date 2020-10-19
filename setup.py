from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='guts',
    version='0.0.0',
    description='A toolbox for code janitors handle git operations '
    + 'withing world of git',
    long_description=readme,
    author='Niko Kivela',
    author_email='niko@tovrleaf.com',
    url='https://github.com/tovrleaf/git-utils',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click==7.1.2'
    ],
    entry_points={
        'console_scripts': [
            'guts=gutscli.guts:main'
        ]
    },
)

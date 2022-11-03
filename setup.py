from eznotes.const import VERSION
from setuptools import find_packages, setup


setup(
    name="eznotes",
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "eznotes = eznotes:main",
            "eznotes-getfull = eznotes.getfull:cli_main",
        ],
    },
)

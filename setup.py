from setuptools import setup, find_packages

setup(
    name="xno",
    version="0.1.0",
    packages=find_packages(include=["xno", "xno.*"]),
    include_package_data=True,
)

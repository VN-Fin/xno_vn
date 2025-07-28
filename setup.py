from setuptools import setup, find_packages


setup(
    name="xno_vn",  # Change to your package name
    version="0.1.0",  # Version of your package
    author="Kim",
    author_email="kim.nguyen@xno.vn",
    description="Quant package for XNO",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VN-Fin/xno_vn",  # GitHub or project link
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",  # Minimum Python version required
)
import numpy
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="compsheet",
    version="1.0.0",
    author="Derek Fujimoto",
    author_email="fujimoto@phas.ubc.ca",
    description="compare microsoft spreadsheet data to check for plagiarism",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dfujim/SpreadsheetPlagiarism",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ),
    install_requires=['openpyxl>=2.5'],
)

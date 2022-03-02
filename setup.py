import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cedar-parsing-utils",
    version="1.0.0",
    author="DataHub",
    author_email="datahub-support@maastrichtuniversity.nl",
    description="This repository hosts all of the parsing utilities for CEDAR schemas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaastrichtUniversity/cedar-parsing-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

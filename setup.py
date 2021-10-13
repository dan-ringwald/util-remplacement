from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='util_replacement',
    version='0.1',
    # scripts=["bin/applymap"] ,
    author="Dan Ringwald",
    author_email="dan.ringwald12@gmail.com",
    description="Utility to apply text replacement from a yaml collection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dan-ringwald/util-remplacement",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
)

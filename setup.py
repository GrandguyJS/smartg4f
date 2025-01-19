from setuptools import setup, find_packages

setup(
    name="smartg4f",
    version="1.2",
    description="Smart g4f provider selector",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="GrandguyJS",
    author_email="grandguymc@gmail.com",
    url="https://github.com/grandguyjs/smartg4f",
    packages=find_packages(),
    install_requires=[
        "g4f"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
import os

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="seriate",
    description="Implementation of the Seriation sequence ordering algorithm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="1.1.2",
    license="Apache-2.0",
    author="source{d}",
    author_email="machine-learning@sourced.tech",
    url="https://github.com/src-d/seriate",
    download_url="https://github.com/src-d/seriate",
    py_modules=["seriate"],
    keywords=["seriation"],
    install_requires=["numpy>=1.0", "ortools>=6.7.4973,<=9", "packaging>=16.0"],
    tests_require=["scipy>=1.0"],
    package_data={"": ["LICENSE.md", "README.md", "requirements.txt"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)

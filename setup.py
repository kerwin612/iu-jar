import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iu-jar",
    version="0.0.5",
    author="ileler",
    author_email="kerwin612@qq.com",
    description="An incremental upgrade tool for jar packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ileler/iu-jar",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    scripts=['iu-jar/iujar'],
)

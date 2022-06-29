from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sense-py",
    version="0.1.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JakeRoggenbuck/sense-py",
    packages=["sense-py"],
    zip_safe=False,
)

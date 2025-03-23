from setuptools import setup

setup(
    name="pyfonts",
    version="0.0.2",
    packages=["pyfonts"],
    description="A simple way to load fonts for matplotlib",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joseph Barbier",
    author_email="joseph.barbierdarnal@gmail.com",
    url="https://github.com/JosephBARBIERDARNAL/pyfonts/",
    install_requires=["matplotlib"],
)

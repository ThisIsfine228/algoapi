from setuptools import setup, find_packages

requirements = ["requests>=2"]

setup(
    name="algoapi",
    version="0.0.1",
    author="Danil Kiselev",
    author_email="danilkiselev2010perm@gmail.com",
    description="Algoritmika api package",
    url="https://github.com/algoapi/homepage/",
    packages=find_packages(),
    install_requires=requirements,
)

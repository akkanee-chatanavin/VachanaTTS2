from setuptools import setup, find_packages

setup(
    name="vachanatts",
    version="2.0.0",
    description="VachanaTTS โมเดล Text-to-Speech สำหรับภาษาไทย",
    url="https://github.com/akkanee-chatanavin/VachanaTTS2",
    packages=find_packages(),
    install_requires=[
        "pythainlp",
        "ssg",
        "requests",
    ],
    python_requires=">=3.8",
)
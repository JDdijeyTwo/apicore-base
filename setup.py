from setuptools import setup, find_packages

setup(
    name="apicore-base",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["requests"],
    author="JDdijey",
    description="APICore BASE - Все продукты APICore!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JDdijeyTwo/apicore-base",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)

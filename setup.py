from setuptools import setup, find_packages

setup(
    name="brownianMotion",
    version="0.1.0",
    description="Brownian Motion Simulation for GSoC-2025 JdeRobot Python Challenge",
    author="Jayzalani",  
    author_email="jayzalani34@gmail.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
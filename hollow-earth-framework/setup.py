#!/usr/bin/env python3
"""
Setup script for Hollow Earth Framework
=======================================

Installation:
    pip install -e .                    # Development install
    pip install .                       # Regular install
    python setup.py install             # Alternative install
    
    # From requirements file
    pip install -r requirements.txt
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
if readme_path.exists():
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = "Mathematical framework for analyzing alternative geological models"

# Read requirements
requirements_path = Path(__file__).parent / "requirements.txt"
if requirements_path.exists():
    with open(requirements_path, "r") as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
else:
    requirements = [
        "numpy>=1.21.0",
        "scipy>=1.7.0", 
        "matplotlib>=3.4.0"
    ]

setup(
    name="hollow-earth-framework",
    version="1.0.0",
    author="Hollow Earth Framework Team",
    author_email="your.email@example.com",  # Replace with actual email
    description="Mathematical framework for analyzing alternative geological models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/hollow-earth-framework",  # Replace with actual URL
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/hollow-earth-framework/issues",
        "Documentation": "https://github.com/yourusername/hollow-earth-framework/docs",
        "Source Code": "https://github.com/yourusername/hollow-earth-framework",
    },
    
    # Package configuration
    packages=find_packages(where="src"),
    package_dir={"": "src"}, 
    python_requires=">=3.8",
    install_requires=requirements,
    
    # Optional dependencies
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "pytest-cov>=2.12.0", 
            "black>=21.6.0",
            "flake8>=3.9.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ],
        "notebook": [
            "jupyter>=1.0.0",
            "jupyterlab>=3.0.0",
        ],
        "advanced": [
            "numba>=0.54.0",
            "cvxpy>=1.1.0",
        ]
    },
    
    # Entry points for command line usage
    entry_points={
        "console_scripts": [
            "hollow-earth=mathematical_framework.core_equations:demonstrate_framework",
            "hollow-earth-demo=__main__:main",
        ],
    },
    
    # Classifiers for PyPI
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research", 
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9", 
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    
    # Keywords for discovery
    keywords=[
        "geophysics", "mathematics", "physics", "modeling",
        "seismology", "waveguide", "fiber-optic", "hollow-earth",
        "gravitational-field", "scientific-computing"
    ],
    
    # Include additional files
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.json", "*.yml", "*.yaml"],
    },
    
    # Zip safe
    zip_safe=False,
)
# src/__init__.py
"""
Hollow Earth Mathematical Framework
==================================

A comprehensive mathematical framework for analyzing alternative geological models,
specifically examining the mathematical viability of hollow Earth configurations.

Key Features:
- Gravitational field calculations for hollow sphere geometry
- Mass conservation and distribution analysis  
- Seismic waveguide modeling (revolutionary fiber optic analogy)
- Thermal gradient analysis
- Inconsistency detection in standard models

Author: Hollow Earth Framework Team
Version: 1.0.0
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Hollow Earth Framework Team"
__license__ = "MIT"

# Import main classes for easy access
try:
    from .mathematical_framework.core_equations import (
        HollowEarthModel,
        SeismicWaveguideModel,
        SphericalShell,
        ModelConfiguration,
        PhysicalConstants,
        CONSTANTS
    )
    
    __all__ = [
        'HollowEarthModel',
        'SeismicWaveguideModel', 
        'SphericalShell',
        'ModelConfiguration',
        'PhysicalConstants',
        'CONSTANTS'
    ]
    
except ImportError:
    # Graceful degradation if dependencies aren't installed
    __all__ = []

# ============================================================================

# src/mathematical_framework/__init__.py
"""
Mathematical Framework Module
============================

Core mathematical implementations for hollow Earth modeling.

This module contains:
- Core equations and physical constants
- Gravitational field calculations
- Seismic wave analysis  
- Optimization algorithms
- Model validation tools
"""

from .core_equations import (
    HollowEarthModel,
    SeismicWaveguideModel,
    SphericalShell, 
    ModelConfiguration,
    PhysicalConstants,
    CONSTANTS,
    demonstrate_framework
)

__all__ = [
    'HollowEarthModel',
    'SeismicWaveguideModel',
    'SphericalShell',
    'ModelConfiguration', 
    'PhysicalConstants',
    'CONSTANTS',
    'demonstrate_framework'
]

# ============================================================================

# src/analysis/__init__.py
"""
Analysis Module
==============

Tools for comparative analysis and visualization.
"""

# Placeholder for future analysis modules
__all__ = []

# ============================================================================

# src/visualization/__init__.py  
"""
Visualization Module
===================

Plotting and visualization tools for model results.
"""

# Placeholder for future visualization modules
__all__ = []
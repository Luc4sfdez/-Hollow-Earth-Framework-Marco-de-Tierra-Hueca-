#!/usr/bin/env python3
"""
Quick Start Example - Hollow Earth Framework
============================================

This script demonstrates the most important features of the framework
in just a few lines of code.

Run this to see:
1. Mass-conserving hollow Earth model
2. Seismic waveguide analysis (fiber optic analogy)
3. Key predictions and comparisons

Usage:
    python examples/quick_start.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from mathematical_framework.core_equations import HollowEarthModel, SeismicWaveguideModel

def main():
    print("🌍 HOLLOW EARTH FRAMEWORK - QUICK START")
    print("=" * 50)
    
    # 1. Create models
    print("\n1️⃣ Creating mathematical models...")
    earth_model = HollowEarthModel()
    waveguide_model = SeismicWaveguideModel()
    
    # 2. Generate optimized hollow Earth configuration
    print("2️⃣ Optimizing hollow Earth configuration...")
    config = earth_model.optimize_for_mass_conservation()
    
    print(f"   ✅ Hollow diameter: {config.central_hollow_radius*2/1000:.0f} km")
    print(f"   ✅ Mass error: {abs(config.total_mass - 5.972e24)/5.972e24*100:.4f}%")
    
    # 3. Analyze seismic waveguide properties (REVOLUTIONARY)
    print("3️⃣ Analyzing seismic waveguide properties...")
    comparison = waveguide_model.analyze_fiber_optic_analogy()
    
    print("   🌐 FIBER OPTIC vs EARTH:")
    print(f"   Fiber critical angle: {comparison['fiber_optic']['critical_angle']:.1f}°")
    print(f"   Earth critical angle: {comparison['earth_seismic']['critical_angle']:.1f}°")
    print(f"   Mechanism: {comparison['comparison']['mechanism']}")
    
    # 4. Show key predictions
    print("4️⃣ Key testable predictions:")
    predictions = waveguide_model.predict_seismic_anomalies()
    for i, prediction in enumerate(predictions[:3], 1):
        print(f"   {i}. {prediction}")
    
    # 5. Compare with observations
    print("5️⃣ Comparison with known phenomena:")
    phenomena = waveguide_model.compare_observed_phenomena()
    
    hum_data = phenomena['earths_hum']
    print(f"   Earth's Hum - Observed: {hum_data['observed']}")
    print(f"   Earth's Hum - Predicted: {hum_data['predicted']}")
    print(f"   Match: {hum_data['match']}")
    
    print("\n" + "=" * 50)
    print("🎉 QUICK START COMPLETE!")
    print("💡 Run 'python src/main.py' for full analysis")
    print("📚 Check README.md for detailed explanations")

if __name__ == "__main__":
    main()
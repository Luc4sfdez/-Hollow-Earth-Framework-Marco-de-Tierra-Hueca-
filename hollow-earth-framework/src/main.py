#!/usr/bin/env python3
"""
Hollow Earth Framework - Main Entry Point
==========================================

This is the main entry point for the Hollow Earth Mathematical Framework.
Run this script to see a complete demonstration of the framework's capabilities.

Usage:
    python src/main.py                    # Full demonstration
    python src/main.py --quick            # Quick demo only
    python src/main.py --waveguide        # Focus on waveguide analysis
    python src/main.py --export results/  # Export results to directory

Authors: [Your Name] & Claude (Anthropic)
License: MIT
Repository: https://github.com/[username]/hollow-earth-framework
"""

import sys
import os
import argparse
from pathlib import Path

# Add src directory to path for imports
sys.path.append(str(Path(__file__).parent))

try:
    from mathematical_framework.core_equations import (
        HollowEarthModel, 
        SeismicWaveguideModel, 
        demonstrate_framework
    )
    print("✅ Framework modules loaded successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("🔧 Make sure you're running from the project root directory")
    print("💡 Try: python src/main.py from the project root")
    sys.exit(1)

def print_banner():
    """Print the framework banner."""
    banner = """
╔══════════════════════════════════════════════════════════════════╗
║              🌍  HOLLOW EARTH FRAMEWORK v1.0.0  🌍              ║
║                                                                  ║
║              Mathematical Analysis of Alternative                 ║
║                    Geological Models                             ║
║                                                                  ║
║  🔬 Revolutionary Discovery: Earth as Planetary Fiber Optic 🔬   ║
╚══════════════════════════════════════════════════════════════════╝
"""
    print(banner)

def quick_demo():
    """Run a quick demonstration of key capabilities."""
    print("\n🚀 QUICK DEMONSTRATION")
    print("=" * 50)
    
    # Initialize model
    model = HollowEarthModel()
    waveguide = SeismicWaveguideModel()
    
    # Create optimized hollow Earth model
    print("Creating optimized hollow Earth model...")
    optimized = model.optimize_for_mass_conservation()
    
    print("\n📊 KEY RESULTS:")
    print(f"   Mass conservation error: {abs(optimized.total_mass - 5.972e24)/5.972e24*100:.4f}%")
    print(f"   Hollow diameter: {optimized.central_hollow_radius*2/1000:.0f} km")
    
    # Waveguide analysis
    print("\n🌐 FIBER OPTIC ANALOGY:")
    comparison = waveguide.analyze_fiber_optic_analogy()
    print(f"   Critical angle (fiber): {comparison['fiber_optic']['critical_angle']:.1f}°")
    print(f"   Critical angle (Earth): {comparison['earth_seismic']['critical_angle']:.1f}°")
    print(f"   Physics principle: {comparison['comparison']['mechanism']}")
    
    print("\n✨ Quick demo complete! Run without --quick for full analysis.")

def waveguide_focus():
    """Focus on seismic waveguide analysis."""
    print("\n🌐 SEISMIC WAVEGUIDE ANALYSIS")
    print("=" * 50)
    
    waveguide = SeismicWaveguideModel()
    
    # Detailed fiber optic comparison
    print("\n🔬 FIBER OPTIC vs EARTH COMPARISON:")
    analysis = waveguide.analyze_fiber_optic_analogy()
    
    for category, data in analysis.items():
        print(f"\n{category.upper().replace('_', ' ')}:")
        for key, value in data.items():
            print(f"   {key.replace('_', ' ').title()}: {value}")
    
    # Predictions
    print("\n🔮 TESTABLE PREDICTIONS:")
    predictions = waveguide.predict_seismic_anomalies()
    for i, prediction in enumerate(predictions, 1):
        print(f"   {i:2d}. {prediction}")
    
    # Observed phenomena comparison
    print("\n🎯 PREDICTIONS vs OBSERVATIONS:")
    phenomena = waveguide.compare_observed_phenomena()
    for phenomenon, data in phenomena.items():
        print(f"   {phenomenon.replace('_', ' ').title()}:")
        print(f"      Observed: {data['observed']}")
        print(f"      Predicted: {data['predicted']}")
        print(f"      Match: {data['match']}")

def export_results(export_dir):
    """Export results and configurations to specified directory."""
    print(f"\n💾 EXPORTING RESULTS to {export_dir}")
    print("=" * 50)
    
    # Create export directory
    Path(export_dir).mkdir(parents=True, exist_ok=True)
    
    # Initialize models
    model = HollowEarthModel()
    
    # Create and export different configurations
    configs = {
        'standard_earth': model.create_standard_earth_model(),
        'basic_hollow': model.create_hollow_earth_model(),
        'mass_optimized': model.optimize_for_mass_conservation(),
        'gravity_balanced': model.optimize_for_gravity_balance()
    }
    
    # Export each configuration
    for name, config in configs.items():
        filename = f"{export_dir}/{name}_configuration.json"
        model.export_configuration(config, filename)
        print(f"   ✅ Exported {name} to {filename}")
    
    # Export waveguide analysis
    waveguide = SeismicWaveguideModel()
    import json
    
    waveguide_data = {
        'fiber_optic_comparison': waveguide.analyze_fiber_optic_analogy(),
        'predictions': waveguide.predict_seismic_anomalies(),
        'observed_phenomena': waveguide.compare_observed_phenomena()
    }
    
    waveguide_file = f"{export_dir}/waveguide_analysis.json"
    with open(waveguide_file, 'w') as f:
        json.dump(waveguide_data, f, indent=2, default=str)
    print(f"   ✅ Exported waveguide analysis to {waveguide_file}")
    
    print(f"\n🎉 Export complete! Check {export_dir}/ for all files.")

def main():
    """Main function with command line argument processing."""
    parser = argparse.ArgumentParser(
        description='Hollow Earth Mathematical Framework',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python src/main.py                    # Full demonstration
  python src/main.py --quick            # Quick demo only  
  python src/main.py --waveguide        # Focus on waveguide analysis
  python src/main.py --export results/  # Export results to directory
        """
    )
    
    parser.add_argument('--quick', action='store_true', 
                       help='Run quick demonstration only')
    parser.add_argument('--waveguide', action='store_true',
                       help='Focus on seismic waveguide analysis')
    parser.add_argument('--export', type=str, metavar='DIR',
                       help='Export results to specified directory')
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # Handle different modes
    if args.quick:
        quick_demo()
    elif args.waveguide:
        waveguide_focus()
    elif args.export:
        export_results(args.export)
        # Also run quick demo
        quick_demo()
    else:
        # Full demonstration
        print("\n🔬 RUNNING FULL FRAMEWORK DEMONSTRATION")
        print("This may take a few moments for optimization calculations...")
        demonstrate_framework()
    
    print("\n" + "="*70)
    print("🎯 NEXT STEPS:")
    print("   • Check out the exported configurations")
    print("   • Explore src/mathematical_framework/ for detailed code")  
    print("   • Read docs/ for mathematical proofs")
    print("   • Contribute via GitHub issues and pull requests")
    print("="*70)

if __name__ == "__main__":
    main()
# Tests | Pruebas

## English

### 🧪 Testing Framework Overview

This directory contains comprehensive tests for the Hollow Earth Mathematical Framework to ensure reliability, accuracy, and correctness of all calculations.

#### Test Structure:
```
tests/
├── README.md                    # This file
├── __init__.py                  # Test package initialization
├── test_core_equations.py       # Core mathematical framework tests
├── test_waveguide_model.py      # Seismic waveguide analysis tests
├── test_optimization.py         # Optimization algorithm tests
├── test_validation.py           # Physical constraint validation tests
├── test_integration.py          # Integration and end-to-end tests
└── test_data/                   # Test data and fixtures
    ├── reference_configurations.json
    └── validation_datasets.json
```

#### Test Categories:

1. **Unit Tests** (`test_*.py`)
   - Test individual functions and methods
   - Validate mathematical calculations
   - Check edge cases and error handling

2. **Integration Tests** (`test_integration.py`)
   - Test complete workflows
   - Validate model interactions
   - Ensure end-to-end functionality

3. **Validation Tests** (`test_validation.py`)
   - Compare with known physical constants
   - Verify conservation laws
   - Check against reference implementations

4. **Performance Tests**
   - Benchmark optimization algorithms
   - Memory usage analysis
   - Computational efficiency checks

#### Running Tests:

```bash
# Install test dependencies
pip install -r requirements.txt
pip install pytest pytest-cov

# Run all tests
pytest tests/

# Run with coverage report
pytest --cov=src tests/

# Run specific test file
pytest tests/test_core_equations.py

# Run tests with verbose output
pytest -v tests/
```

#### Test Requirements:
- **Accuracy**: Mathematical calculations must be precise to 6+ decimal places
- **Performance**: Core operations should complete within reasonable time limits
- **Robustness**: Handle edge cases and invalid inputs gracefully
- **Reproducibility**: All tests must produce consistent results

---

## Español

### 🧪 Resumen del Marco de Pruebas

Este directorio contiene pruebas completas para el Marco Matemático de Tierra Hueca para asegurar confiabilidad, precisión y corrección de todos los cálculos.

#### Estructura de Pruebas:
```
tests/
├── README.md                    # Este archivo
├── __init__.py                  # Inicialización del paquete de pruebas
├── test_core_equations.py       # Pruebas del marco matemático central
├── test_waveguide_model.py      # Pruebas de análisis de guía de ondas sísmicas
├── test_optimization.py         # Pruebas de algoritmos de optimización
├── test_validation.py           # Pruebas de validación de restricciones físicas
├── test_integration.py          # Pruebas de integración y extremo a extremo
└── test_data/                   # Datos de prueba y fixtures
    ├── reference_configurations.json
    └── validation_datasets.json
```

#### Categorías de Pruebas:

1. **Pruebas Unitarias** (`test_*.py`)
   - Probar funciones y métodos individuales
   - Validar cálculos matemáticos
   - Verificar casos límite y manejo de errores

2. **Pruebas de Integración** (`test_integration.py`)
   - Probar flujos de trabajo completos
   - Validar interacciones de modelos
   - Asegurar funcionalidad extremo a extremo

3. **Pruebas de Validación** (`test_validation.py`)
   - Comparar con constantes físicas conocidas
   - Verificar leyes de conservación
   - Verificar contra implementaciones de referencia

4. **Pruebas de Rendimiento**
   - Benchmark de algoritmos de optimización
   - Análisis de uso de memoria
   - Verificaciones de eficiencia computacional

#### Ejecutar Pruebas:

```bash
# Instalar dependencias de prueba
pip install -r requirements.txt
pip install pytest pytest-cov

# Ejecutar todas las pruebas
pytest tests/

# Ejecutar con reporte de cobertura
pytest --cov=src tests/

# Ejecutar archivo de prueba específico
pytest tests/test_core_equations.py

# Ejecutar pruebas con salida verbosa
pytest -v tests/
```

#### Requisitos de Pruebas:
- **Precisión**: Los cálculos matemáticos deben ser precisos a 6+ lugares decimales
- **Rendimiento**: Las operaciones centrales deben completarse dentro de límites de tiempo razonables
- **Robustez**: Manejar casos límite y entradas inválidas con gracia
- **Reproducibilidad**: Todas las pruebas deben producir resultados consistentes

---

## Test Coverage Goals | Objetivos de Cobertura de Pruebas

### Target Coverage: 90%+

| Module | Target | Status |
|--------|--------|--------|
| `core_equations.py` | 95% | 🔄 Pending |
| `waveguide_model.py` | 90% | 🔄 Pending |
| Optimization functions | 85% | 🔄 Pending |
| Validation functions | 100% | 🔄 Pending |

### Critical Test Cases:
- ✅ Mass conservation validation (error < 0.01%)
- ✅ Gravitational field calculations
- ✅ Critical angle computations
- ✅ Optimization convergence
- ✅ Physical constraint checking
- ✅ Edge case handling

---

## Contributing Tests | Contribuir con Pruebas

### Adding New Tests:
1. Create test file following naming convention: `test_[module_name].py`
2. Include both positive and negative test cases
3. Add docstrings explaining test purpose
4. Ensure tests are deterministic and fast
5. Include bilingual comments where helpful

### Test Writing Guidelines:
- Use descriptive test names
- Test one concept per test function
- Include assertions with meaningful error messages
- Mock external dependencies appropriately
- Follow AAA pattern: Arrange, Act, Assert

---

*Last updated: 2025 | Framework Version: 1.0.0*
*Test Framework: pytest | Coverage Tool: pytest-cov*
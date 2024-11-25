# Variable para el directorio donde están los tests
TEST_DIR = ml-service

# Variable para el ejecutor de pruebas (puedes usar pytest o unittest)
TEST_RUNNER = pytest



install:
	pip install -r requirements.txt
lint:
	pylint --disable=R,C $(TEST_DIR)/*.py
# Objetivo para ejecutar los tests
test:
	@echo "Running tests in $(TEST_DIR)..."
	cd ml-service && pytest

# Objetivo para ejecutar todos los tests en el directorio
test-all:
	@echo "Running all tests in $(TEST_DIR)..."
	$(TEST_RUNNER) $(TEST_DIR)

# Limpieza (opcional, si necesitas limpiar algún archivo temporal)
clean:
	@echo "Cleaning up..."
	rm -rf __pycache__ $(TEST_DIR)/__pycache__

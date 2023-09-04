VENV_PATH = "venv/Scripts/activate"

test:
	pytest .
	
quality_check:
	isort .
	black .
	python -m pylint --recursive=yes *.py 

activate_venv: venv
	@echo "Activating virtual environment..."
	@source ${VENV_PATH}




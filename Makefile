VENV_PATH = "venv/Scripts/activate"

test:
	pytest .
	
quality_check:
	isort .
	black .
	python -m pylint --recursive=yes *.py 

load_data:
	python load_iris_data.py
	@echo "finished loading"
	echo "last message of load_data"

activate_venv: venv
	@echo "Activating virtual environment..."
	@source ${VENV_PATH}




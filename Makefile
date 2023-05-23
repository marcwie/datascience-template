install:
	poetry install

activate:
	poetry shell

output:
	sh scripts/execute_notebooks.sh

.PHONY: output

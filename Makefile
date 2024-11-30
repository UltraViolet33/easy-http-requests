test:
	poetry run pytest tests

test-coverage:
	poetry run pytest --cov=easy_http_requests

docs:
	cd docs && make html
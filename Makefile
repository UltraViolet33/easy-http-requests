test:
	poetry run pytest tests

test-coverage:
	poetry run pytest --cov=easy_http_requests --cov-report=term-missing

documentation:
	sphinx-apidoc -o docs/source easy_http_requests && cd docs && make html

lint-black:
	poetry run black --check easy_http_requests tests

black:
	poetry run black easy_http_requests tests

check-type:
	poetry run mypy easy_http_requests tests
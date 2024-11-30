test:
	poetry run pytest tests

test-coverage:
	poetry run pytest --cov=easy_http_requests

docs:
	cd docs && make html

lint-black:
	black --check easy_http_requests tests

black:
	poetry run black easy_http_requests tests

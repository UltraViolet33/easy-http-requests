test:
	poetry run pytest tests

test-coverage:
	poetry run pytest --cov=easy_http_requests --cov-report=term-missing

documentation:
	poetry run sphinx-apidoc -o docs/source easy_http_requests
	poetry run sphinx-build -b html docs/source docs/build/html

lint-black:
	poetry run black --check easy_http_requests tests

black:
	poetry run black easy_http_requests tests

check-type:
	poetry run mypy easy_http_requests tests

make-minor:
	poetry version minor

make-patch:
	poetry version patch

make-major:
	poetry version major
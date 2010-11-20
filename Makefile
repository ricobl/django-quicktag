test: clean
	@python manage.py test
clean:
	@find . -name "*.pyc" -delete
	@rm -rf .coverage htmlcov/
	@rm -rf build/ dist/ *.egg-info
install: clean
	@python setup.py install
	@rm -rf build/ dist/ *.egg-info
uninstall:
	@pip uninstall django-quicktag
register:
	python setup.py register
upload:
	python setup.py sdist upload --show-response

test: clean
	@python manage.py test
clean:
	@find . -name "*.pyc" -delete
install:
	@python setup.py install
	@rm -rf build/ dist/ *.egg-info
uninstall:
	@pip uninstall django-quicktag
upload:
	@sudo python setup.py sdist upload --show-response

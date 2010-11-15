# Django settings for testproject project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = '@d(%kjlm=@8g+!nf+-(7$6+mtl&p-4-4#q$hu2pe0obegok7lw'

# List of callables that know how to import templates from various sources.
#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.load_template_source',
#    'django.template.loaders.app_directories.load_template_source',
#)

#MIDDLEWARE_CLASSES = (
#    'django.middleware.common.CommonMiddleware',
#)

ROOT_URLCONF = 'testproject.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEST_RUNNER = 'nose_runner.run_tests'
NOSE_ARGS = ['-sd', '--verbose', '--with-coverage', '--cover-package=quicktag']

INSTALLED_APPS = (
    'dummyapp',
)

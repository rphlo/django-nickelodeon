import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'nickelodeon.site.settings'
test_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, test_dir)

from django import setup as django_setup
from django.test.utils import get_runner
from django.conf import settings


def runtests():
    django_setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['nickelodeon'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    runtests()

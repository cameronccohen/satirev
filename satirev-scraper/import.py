#import django
#from satirev import settings
#from satirev.articles.models import MyModel

import sys
import os
import django

sys.path.append('your_project_directory')
os.environ['DJANGO_SETTINGS_MODULE'] = 'satirev.settings'
django.setup()

from satirev.articles.models import Tag
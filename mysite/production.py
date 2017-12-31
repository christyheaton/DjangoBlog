from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['ec2-54-201-72-130.us-west-2.compute.amazonaws.com', 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

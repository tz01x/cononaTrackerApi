from .settings import  BASE_DIR
import  os
STATIC_URL = '/static/'
MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static','static_dir'),
]
STATIC_ROOT = os.path.join(BASE_DIR,'static','static_root','static')

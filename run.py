import os
from waitress import serve
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# carga django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')
application = get_wsgi_application()

# ruta statics
application = WhiteNoise(application, root=settings.STATIC_ROOT)

if __name__ == '__main__':
    print("Servidor iniciado..")
    serve(application, host='0.0.0.0', port=8000, threads=4)
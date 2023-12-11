
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from django.core.asgi import get_asgi_application


import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_1.settings')

application = get_asgi_application()

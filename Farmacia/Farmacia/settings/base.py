from pathlib import Path
import os
from  django.core.exceptions import ImproperlyConfigured
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open("secret.json") as f:
  secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg ="la variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)
    
SECRET_KEY= get_secret('SECRET_KEY')

# # Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aplicaciones.Comunidad',
    'aplicaciones.Productos',
    'aplicaciones.Movimientos'
]



JAZZMIN_SETTINGS = {
    "site_logo": "farmacia.png",
    "login_logo": "farmacia.png",
    "site_icon": "farmaa.png", 
    "site_title": "Farmacia Mutual",
    "site_header": "Farmacia Mutual",
    "site_brand": "Farmacia Mutual",
    "welcome_sign": "Bienvenido a la Farmacia Mutual",
        "Comunidad.Proveedor": "fas fa-users",
    "order_with_respect_to": ["auth.user", "auth.Group", "Productos.Producto", "Movimientos.Entrada","Movimientos.Salida","Comunidad.Empleado","Comunidad.Paciente","Comunidad.Proveedor","Comunidad.Laboratorio","Comunidad.direccion","Comunidad.telefono"],
    "show_ui_builder": False,
    "topmenu_links": [
        {"name": "Support","url": "http://superiorlapaz.edu.ar/", "new_window": True}, 
    ],
    "icons":{
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "Comunidad.direccion":"fas fa-circle",
        "Comunidad.Empleado": "fas fa-user",
        "Comunidad.Paciente": "fas fa-hospital-user",
        "Comunidad.Proveedor": "fas fa-users",
        "Comunidad.Laboratorio":"far fa-building",
        "Comunidad.telefono": "fas fa-phone",
        "Movimientos.Movimiento": "fas fa-chevron-circle-right",
        "Productos.Producto":"fas fa-pills",
      
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Farmacia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Farmacia.wsgi.application'



SECRET_KEY = 'o$!!^76&1&(2ghcg35!))uakc9$d21=9f@8^_vdgk*1(w#^wj*'


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_service.db.user_models'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'userDB',
    'USER': 'root',
    'PASSWORD': 'dwarkamai',
    'HOST': 'localhost',
    'PORT': '',
},
}

from .base import settings

settings['debug'] = False

DATABASES = {
    'default': 'mssql+pymssql://loja200:loja200@s500sqldev01.magazineluiza.intranet:1433/'
}
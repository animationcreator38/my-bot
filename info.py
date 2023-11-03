from os import environ

API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
FILE_CAPTION = environ.get('FILE_CAPTION', '<code>{file_name}</code>')
OWNER = int(environ.get('OWNER', ''))
PRIVATE_BOT = bool(environ.get('PRIVATE_BOT', True))

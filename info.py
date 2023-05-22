from os import environ

API_ID = int(environ.get('API_ID', '28103752'))
API_HASH = environ.get('API_HASH', '479579601469809b9a9c8ffc15fbe11a')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
FILE_CAPTION = environ.get('FILE_CAPTION', '<code>{file_name}</code>')
OWNER = int(environ.get('OWNER', '1977238156'))
PRIVATE_BOT = bool(environ.get('PRIVATE_BOT', False))

from os import environ

API_ID = int(environ.get('API_ID', '882399cfe65fdec68e451e4a6eb246d3'))
API_HASH = environ.get('API_HASH', '21761864')
BOT_TOKEN = environ.get('BOT_TOKEN', '6135291343:AAF4f5HfmjwtTD-Ffk3HuVW_7PYJVEDTKjk')
FILE_CAPTION = environ.get('FILE_CAPTION', '<code>{file_name}</code>')
OWNER = int(environ.get('OWNER', '6371417316'))
PRIVATE_BOT = bool(environ.get('PRIVATE_BOT', True))

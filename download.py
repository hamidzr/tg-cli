from telethon import TelegramClient, sync, events

# local imports
import config
from cli import args

api_id, api_hash = config.creds
with TelegramClient('mySession', api_id, api_hash) as client:
  print('logged in as', client.get_me().username)

  msgs = client.get_messages(f'@{args.username}', limit=10)
  for msg in msgs:
    if msg.document is not None:
      for attr in msg.document.attributes:
        if hasattr(attr, 'file_name'):
          print(attr.file_name)
          # client.download_media(message=msg)

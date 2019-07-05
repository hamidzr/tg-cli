from telethon import TelegramClient, events, sync

# local imports
import config
from cli import args

api_id, api_hash = config.creds
with TelegramClient('mySession', api_id, api_hash) as client:
  print('logged in as', client.get_me().username)

  if args.text:
    client.send_message(f'@{args.username}', args.text)
  if args.file:
    client.send_file(f'@{args.username}', args.file,
                     force_document = True, caption = args.caption)

import slack
import os
from dotenv import load_dotenv
from send_message import *

load_dotenv(dotenv_path = './.env')

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

client = slack.WebClient(token=os.environ["SLACK_BOT_TOKEN"])

send_message(client)
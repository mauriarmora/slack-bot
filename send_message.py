import datetime as dt
import random
import json

with open('teamMembers.json') as json_file:
  team_members = json.load(json_file)

team_names = ['James Fabbi', 'Bahaa Badran', 'Anthony Cammisano', 'Dominique Ducharme', 'Jack Dundas', 'Anthony Najjar']

def send_message(client):
  # client.chat_postMessage(channel='#happy-bot-mauri', text=random.choice(messages))
  
  beginning = dt.datetime.now()
  t = dt.datetime.now()
  
  while t.second - beginning.second  != 12:
    random_num = random.choice([0, 1])
    random_member = random.choice(team_names)
    count = dt.datetime.now().second - t.second
    if count >= 1:
      # client.chat_postMessage(channel='#happy-bot-mauri', text=random.choice(messages))
      print(team_members[random_member][random_num])
      
      t = dt.datetime.now()
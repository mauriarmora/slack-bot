import datetime as dt
import random
import json

with open('teamMembers.json') as json_file:
  team_members = json.load(json_file)

# Saving names to find each of them in the JSON file
TEAM_NAMES = ['James Fabbi', 'Bahaa Badran', 'Anthony Cammisano', 'Dominique Ducharme', 'Jack Dundas', 'Anthony Najjar']

# Creating the function that will be called from the slack-bot.py file
def send_message(client):
  # Setting the time when the app starts running to calculate the 2h time.
  beginning = dt.datetime.now()

  # Setting the time for the first time, wich will be changed later to calculate the 10s
  t = dt.datetime.now()
  
  # Create a while loop to keep posting every 10m until it reaches 120m
  while t.second - beginning.second  != 120:
    # Picking random name from the array, and random number between 0 and 1 to pick a sentence
    random_num = random.choice([0, 1])
    random_member = random.choice(TEAM_NAMES)

    # Counting the 10s with the current time and the t variable
    count = dt.datetime.now().second - t.second

    if count >= 1:
      random_cumpliment = team_members[random_member][random_num]
      # client.chat_postMessage(channel='#happy-bot-mauri', text=team_members[random_member][random_num])
      print(random_cumpliment)

      # Resetting the t variable to calculate the 10s
      t = dt.datetime.now()
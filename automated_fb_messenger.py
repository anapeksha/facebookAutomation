import fbchat
import json
from getpass import getpass
import time


cookies = {}
try:
    # Load the session cookies
    with open('session.json', 'r') as f:
        cookies = json.load(f)
except:
    # If it fails, never mind, we'll just login again
    pass

username = input("Username:- ")
client = fbchat.Client(username, getpass(), session_cookies=cookies)

# Client work
name = input("Search for a friend: ")
friends = client.searchForUsers(name)
friend = friends[0]
msg = input("Type the message: ")
sent = client.sendMessage(msg, thread_id=friend.uid)
time.sleep(5)
if sent:
    print("Message sent successfully!!")

# Saving session cookies

with open('session.json', 'w') as f:
    json.dump(client.getSession(), f)
    client.logout()


       

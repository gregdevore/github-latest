import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: main.py username')
        sys.exit()

    username = sys.argv[1]
    response = requests.get('https://api.github.com/users/{}/events'.format(username))
    if response.status_code == 200: # Make sure OK response received
        latest_event = response.json()[0]
        event_id = latest_event['id']
        event_type = latest_event['type']
        event_timestamp = latest_event['created_at']
        print('User {} created event {} of type \'{}\' at {}'.format(username,
                                                                     event_id,
                                                                     event_type,
                                                                     event_timestamp))
    else:
        print('Error, response code of {:d} received. Unable to proceed'.format(response.status_code))

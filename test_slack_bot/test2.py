import os

import websocket
from slacker import Slacker

token = os.environ['SLACK_TOKEN']
slack = Slacker(token)

response = slack.rtm.start()
sock_endpoint = response.body['url']
slack_socket = websocket.create_connection(sock_endpoint)

slack_socket.recv()

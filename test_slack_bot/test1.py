import os

from slacker import Slacker

token = os.environ['SLACK_TOKEN']
slack = Slacker(token)
slack.chat.post_message('#test-bot', 'test')

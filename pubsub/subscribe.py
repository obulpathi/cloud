import time
from gcloud import pubsub

client = pubsub.Client(project='thedataclouds')
topic = client.topic('mytopic234')

subscription = topic.subscription('mysubscriber234')

while True:
    try:
        messages = subscription.pull()
        for ackid, message in messages:
            print message.data

        subscription.acknowledge([ackid for ackid, _ in messages])
    except:
        time.sleep(1)

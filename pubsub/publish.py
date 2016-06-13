import time

from gcloud import pubsub

client = pubsub.Client(project='thedataclouds')
topic = client.topic('mytopic234')

for i in range(10):
    topic.publish('Hello ' + str(i) + '!')
    time.sleep(1)

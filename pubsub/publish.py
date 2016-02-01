import time

from gcloud import pubsub

client = pubsub.Client(project='thedatalabproject')
topic = client.topic('mytopic')

for i in range(10):
    topic.publish('Hello ' + str(i) + '!')
    time.sleep(1)

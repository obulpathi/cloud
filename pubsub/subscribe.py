from gcloud import pubsub

client = pubsub.Client(project='thedatalabproject')
topic = client.topic('mytopic')

subscription = topic.subscription('mysubscriber')

messages = subscription.pull()

for ackid, message in messages:
    print message.data

subscription.acknowledge([ackid for ackid, _ in messages])

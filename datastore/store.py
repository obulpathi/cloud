from gcloud import datastore


dataset = datastore.Client(project='thedatalabproject')

entity = datastore.Entity(key=dataset.key('Greeting'))
entity['message'] = 'Hello, world!'

dataset.put(entity)

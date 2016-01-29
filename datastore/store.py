from gcloud import datastore


dataset = datastore.Client(dataset_id='obulpathinew')

entity = datastore.Entity(key=dataset.key('Greeting'))
entity['message'] = 'Hello, world!'

dataset.put(entity)

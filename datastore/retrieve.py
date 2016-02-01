from gcloud import datastore


dataset = datastore.Client(project='thedatalabproject')

query = dataset.query(kind='Greeting')
for result in query.fetch():
    print(result)

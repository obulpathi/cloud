from gcloud import datastore


dataset = datastore.Client(dataset_id='obulpathinew')

query = dataset.query(kind='Greeting')
for result in query.fetch():
    print(result)

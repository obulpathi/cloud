import mlapi as api

text = 'Tom Sawyer is a book written by a guy known as Mark Twain.'

result = api.entities(text)
print(result)

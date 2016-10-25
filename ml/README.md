# Cloud ML

## Python
To use APIs through Python, use Python wrappers with default account.

## APIs:
For accessing APIs directly through curl or Postman use the following procedure.

```
cloud config configurations create services
cloud config configurations activate services
```

Go to APIs and enable language / speech / vision APIs
Create credentials: Create a service account to access the API
Save json file as ~/.cloud/ml-apis.json

```
export GOOGLE_APPLICATION_CREDENTIALS=~/.cloud/ml-apis.json
cloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
export TOKEN=`cloud auth print-access-token`
curl -s -k -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOKEN" \
    https://language.googleapis.com/v1beta1/documents:analyzeEntities \
    -d @entity-request.json
```

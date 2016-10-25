# For API access:

Commands:
- cloud config configurations create services
- cloud config configurations activate services

Go to APIs and enable language API

Create credentials: Create a service account to access the API

Save json file in the ~/.cloud folder

export GOOGLE_APPLICATION_CREDENTIALS=~/.cloud/bitlabs-mlapis.json

cloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

cloud auth print-access-token

curl -s -k -H "Content-Type: application/json" \
    -H "Authorization: Bearer TOKEN" \
    https://language.googleapis.com/v1beta1/documents:analyzeEntities \
    -d @entity-request.json

# Or, use Google Cloud and the wrapper scripts.

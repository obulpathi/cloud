cloud docker build -t gcr.io/$PROJECT_ID/hello-node:v1 .

cloud docker run -d -p 8080:8080 --name node gcr.io/$PROJECT_ID/hello-node:v1

cloud docker stop node

cloud docker push gcr.io/$PROJECT_ID/hello-node:v1

################################################################################

cloud config set compute/zone us-central1-a

cloud container clusters create hello-world

cloud container clusters get-credentials hello-world

cloud docker build -t gcr.io/$PROJECT_ID/hello-node:v1 .

cloud docker run -d -p 8080:8080 --name node gcr.io/$PROJECT_ID/hello-node:v1

cloud docker stop node

cloud docker push gcr.io/$PROJECT_ID/hello-node:v1

################################################################################

node server.js
cloud docker run -d -p 8080:8080 --name node gcr.io/$PROJECT_ID/hello-node:v1
cloud docker stop node

cloud config set compute/zone us-central1-a

cloud container clusters create hello-world

cloud container clusters get-credentials hello-world

kubectl run hello-node --image=gcr.io/$PROJECT_ID/hello-node:v1 --port=8080

kubectl get deployments

kubectl get pods

kubectl expose deployment hello-node --type="LoadBalancer"

kubectl scale deployment hello-node --replicas=4

kubectl get deployments

kubectl get pods

################################################################################

response.end('Hello Kubernetes World!');

docker build -t gcr.io/$PROJECT_ID/hello-node:v2 .
cloud docker push gcr.io/$PROJECT_ID/hello-node:v2

kubectl set image deployment/hello-node hello-node=gcr.io/$PROJECT_ID/hello-node:v2
kubectl get deployments

################################################################################

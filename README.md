# Assignment 1: Build Something

## Introduction

This is a simple example of a distributed architecture that usese microservices to fetch data from a database and show it to the user using a web app.

## Components

### Front-end

The front-end consists of a Flask web server that displays a simple site where the user can input a number (from 1 to 50) and get a random sample of fake contact information.

### Back-end

Similarly to the front-end it is a Flask server that takes the request from the front-end, contacts the database using psycopg2 and retrieves the requested number of samples.

### Database

Contact information is stored in a PostgreSQL database populated with contact information generated with Faker.

## Running with docker compose

The required Docker images are available in Docker Hub. The system can be started by running 

```bash
docker compose up
```

Once running, you can access the front-end from a web browser using port 5000.

## Running with Kubernetes

NOTE: Kubernetes configuration files have been created using [kompose](https://kompose.io/).

For local testing first start minikube with the command

```bash
minikube start
```

Then, use `kubectl` to apply all the deployment and service information in the `kompose` file. This can be done with the command

```bash
kubectl apply -f kompose/
```

To verify that everything is working correctly, you can use the commands `kubectl get pods` and `kubectl get services` to check that the containers are running.

To access the front-end, you first need to expose it. This can be done using the command

```bash
minikube service front-end-tcp
```

Running this command should open your default web browser in the correct URL and port. Otherwise, the information will be displayed in the terminal.

The number of replicas can be changed using the following command

```bash
kubectl scale deployment backend --replicas=3
```

In this case, the number of backends has been increased from the default 1 to 3. 

This action can be verified running the command `kubectl get pods` once more. This time you should see multiple instances of the backend. Using the web browser to get retrieve information should still work as expected.

Finally, the system can be stopped by running 

```bash
kubectl delete -f kompose/
```

Minikube can also be stopped with the command

```bash
minikube delete
```



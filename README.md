# NLP As A Microservice

![NLP As A Microservice Demo](https://github.com/karndeb/Fastapi-Streamlit-NLPService/blob/master/demo/animation_demo2.gif)

This project is a sample demo of NLP as a service mono-repo microservice platform built using FastAPI, Streamlit and Hugging Face.
The use cases are related to chatbot automation services. 


## Use Cases

- Next Query Recommendation
- Query Expansion
- Fallback Reduction

## Features
 - Files Upload and Download integrated with s3
 - Services are in a mono repo microservice pattern 
 - Temporary and secured access to users for downloading processed files from s3 using presigned urls
 - Dockerized application. Indiviual docker containers for each microservice
 - Nginx Reverse Proxy to ensure security, scalability, flexibilty and web acceleration
 - Microservice specific CI/CD using AWS Codecommit, CodePipeline
 - AWS EKS Fargate serverless deployment. Microservice specific deployment, service and ingress manifests provided

## Requirement

Please add `AWS_SECRET_ACCESS_KEY` and `AWS_ACCESS_KEY_ID` in the `helpers.py` in each indiviual microservice

## Installation & Usage

```bash
$ git clone  https://github.com/karndeb/Fastapi-Streamlit-NLPService.git
# Use docker compose to start the services
$ docker-compose up
# Start the Streamlit server
$ streamlit run app.py
```

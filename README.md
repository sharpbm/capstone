[![CircleCI](https://dl.circleci.com/status-badge/img/gh/sharpbm/capstone/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/sharpbm/capstone/tree/main)

# Project Overview
This is a simple flasked based python application, deployed on AWS EKS. In this project I applied the skills learned throughout the Cloud DevOps Nanodegree program.

# Techstack & Platform Used
* Amazon AWS - Cloud services
* CloudFormation - Infrastructure as Code
* Docker Hub - Container images repository service
* Circle CI - Cloud-based CI/CD service
* AWS EKS - Amazon Elastic Kubernetes Services
* AWS eksctl - The official CLI for Amazon EKS
* AWS CLI - Command-line tool for AWS
* kubectl - a command-line tool to control Kubernetes clusters

# Pre-Requisites
* CircleCI Account
* AWS Account
* Docker Hub Account

# CircleCI Pipeline Environment
Setup Following Environment Variable
    * AWS_ACCESS_KEY_ID
    * AWS_DEFAULT_REGION
    * AWS_SECRET_ACCESS_KEY
    * AWS_SESSION_TOKEN
Setup SSH Key For EC2 Login

# CI/CD Jobs
* run-lint - Lint Python & Docker 
* build-upload-docker - Build Docker Image & Push it to Docker Hub
* create-eks-cluster - Create EKS Cluster using EKSCTL
* create-developer-vm - Create an EC2 VM and install AWSCLI & KUBECTL using Ansible. This VM can be used by developers to interact with EKS Cluster
* deploy-app - Deploy application on EKS Cluster and expose it through Loadbalancer
* smoke-test - Test the application is deployed successfully


# Application Url
${loadbalancer}:8080/captone-app






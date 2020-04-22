#!/bin/bash

#adds bitnami repo
helm repo add bitnami https://charts.bitnami.com/bitnami

#install rabbitmq
helm install --generate-name --set rabbitmq.username=admin,rabbitmq.password=secretpassword,rabbitmq.erlangCookie=secretcookie bitnami/rabbitmq

#notes

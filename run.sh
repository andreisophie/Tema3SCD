#!/bin/bash

docker swarm init
docker build . -t tema3scd_adapter
docker stack deploy -c stack.yml tema3scd
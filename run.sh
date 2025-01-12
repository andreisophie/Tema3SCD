#?/bin/bash

docker swarm init --advertise-addr 10.255.255.254
docker build . -t tema3scd_adapter
docker stack deploy -c stack.yml tema3scd
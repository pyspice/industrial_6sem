docker-machine create --driver virtualbox default
docker-machine env default | Invoke-Expression
docker pull mongo
docker pull rabbitmq
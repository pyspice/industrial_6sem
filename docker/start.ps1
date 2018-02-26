docker-machine start default
docker-machine env default | Invoke-Expression
docker-compose build
docker-compose up -d db queue
sleep(10)
docker-compose up client server
docker-machine create --driver virtualbox default
docker-machine start default | Invoke-Expression
docker-compose build
echo To open edit page, type "http://<IP>:8000/admin/todos/todo/" in browser search bar, IP:
docker-machine ip default                
echo login: roach
echo password: roach123 
echo To open TODO list page, type "http://<IP>:8000/todos/"
docker-compose up
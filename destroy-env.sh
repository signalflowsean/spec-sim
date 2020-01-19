docker-compose down --remove-orphans
docker ps
docker image rm -f spec-sim_server
docker image rm -f spec-sim_tests 
docker image rm -f spec-sim_client 
docker images 
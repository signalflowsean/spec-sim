docker-compose down
docker ps
docker image rm -f spec-sim_api
docker image rm -f spec-sim_tests 
docker image rm -f spec-sim_client 
docker image rm -f spec-sim_db
docker images 
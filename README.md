# Spectral Similarity 

## Set up local enviroment
**To set up a local environment run command:** `./build-env.sh`

*Note:* if you run into permission issues please see the [useful commands section](#useful-commands)</a>

**To destory/remove the local environment run command:** `./destroy-env.sh`

<a name="useful-commands"></a>
## Useful Commands
**Setting up permissions on a script:** `chmod +x script.sh`b

## Connect to DB
*To enter the db container:* `docker exec -it spec-sim_db_1 bash`
*To enter the sql shell:* `mysql -u spec-sim -proot spec-sim`

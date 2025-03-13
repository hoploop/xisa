# Cert service

This service provides the ability to generate openssl server and client certificates locally.
The run.sh command generates all required openssl files inside the folder `shared`.

## Docker-compose

* In order to run correctly this service, you need to create the folder: `secrets/cert` inside your `services` folder
* To run this service simply type: `docker-compose run cert`
## About this project

This project contains instructions and code for a simple, small stand-alone web application meant to run within a docker instance.

## Getting Started

Please follow the below instructions to set this project locally.


### Prerequisites

NOTE: This project was built and tested in the following environment, your mileage may vary (as docker operates with different dependencies on different kernel and OS versions). The following are required installations to run the project.

- OS: Debian
- Kernel Version: 5.10

* docker 
  The instructions found [here](https://docs.docker.com/engine/install/debian/) were used to install docker for the above environment.

* docker-compose
  Installation instructions found [here](https://docs.docker.com/compose/install/).


### Installation 

1. Download this repository.
2. Verify docker and docker-compose are installed.
3. Download the GeoLite2-City.mmdb database from Maxmind [here](https://www.maxmind.com/en/geolite2/signup?lang=en) and place it into the `./app/static/` directory.

This should be all that is required to get started.

## Usage

The following commands can be used to deploy, interact, or work with the container.

`docker-compose up` can be used to build and start the container (for the first time)
`docker-compose down` can be used to stop the container

If wanting to deploy the container instance as a daemon, `docker-compose up -d` can be used. However, since there is no default hosting IP specified in the docker-compose file, one would need to specify it before launching this command.

If wanting to add additional code to this project, this can also be achieved. If you have already built the project once, `docker-compose up --build --force-recreate` can be used to rebuild the project and deploy it in one command. Make sure the existing container has been stopped by running `docker compose down`.

Upon deploying, the docker-compose debug log will state the IP the web app will run on as well as the port, which is set to 5000 in the docker-compose file i.e. `http://<IP>:5000`.

## Testing

Tests are located in `app/tests/`.

There are two ways to run tests.

A. 
  1. Start the container instance with `docker-compose up` from the root of the project directory. 

  2. In another terminal window, run `docker ps` to obtain the container id of the running instance.

  3. Get shell access within the container by running `docker exec -it <CONTAINER_ID> sh`. This will drop you into the root of the project inside of the container.

  4. Run `pytest`

B. (Optional)
  1. Start the container instance with `docker-compose up` from the root of the project directory. Note down the exposed IP.  

  2. On your local system, have `pip` installed and download the following packages like so: `pip install requests && pip install pytest && pip install coverage`.

  3. Modify the `app/tests/test_strings.py` file by replacing each occurrence of localhost with with the exposed IP from step one.

  4. Run `pytest` within project folder.


## Other

Other improvements can be made, such as the following, but were not specified as part of the project requirements:

- The addition of a self signed ssl cert, to secure traffic between client and server (especially so given that there is form input).

- The ability to run on a more production-esque, fault tolerant server, such as NGINX using the uwsgi deployment option.

- Under normal circumstances, Flask would not be used for production grade services - as it is a micro framework, but was fitting for this small project.

- Several others come to mind, but were not necessarily part of the project scope and can be discussed later.


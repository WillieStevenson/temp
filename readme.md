## About this project

This project contains instructions and code for a simple, small stand-alone web application meant to run within a docker instance.

## Getting Started

Please follow the below instructions to set this project locally.


### Prerequisites

NOTE: This project was built and tested in the following environment, your milage may vary (as docker operates with different dependencies on different kernel and OS versions). The following are required installations to run the project.

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

If wanting to add additional code to this project, this can also be achieved. If you have already built the project once, `docker-compose up --build --force-recreate` can be used to rebuild the project and deploy in one command.





## Acknowledgements


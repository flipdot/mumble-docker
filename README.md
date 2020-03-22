# Mumble-Docker

Batteries-included hosting template for docker-compose instance of [Mumble/Murmur](https://github.com/flipdot/mumble) and [botamusique](https://github.com/azlux/botamusique).

## Prequisites

- Git
- Docker
- docker-compose
- Certbot (optional) for running this in productive with TLS

## Installation

1. Clone this repo and it's submodules
1. Adapt the config for [Mumble](data/config.ini) and [botamusique](botamusique-docker/configuration.ini) to your needs
1. Spin up the containers. On the first run the images are build, so it may take some time

```bash
git clone --recurse-submodules git@github.com:flipdot/mumble-docker.git
cd mumble-docker
docker-compose up
```

## Local development

If you want to develop on these yourself, you will need to build the containers locally.
To do this, open up `docker-compose.yaml`, comment out the `image:` lines, and un-comment the `build:` lines.

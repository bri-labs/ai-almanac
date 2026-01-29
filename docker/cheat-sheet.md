# Docker Cheat Sheet

## Table of Contents
- [Image & Containers](#image--containers)
  - [Images](#images)
  - [Containers](#containers)
- [Working With Files](#working-with-files)
- [Ports & Networking](#ports--networking)
- [Cleanup](#cleanup)
- [Docker Compose](#docker-compose)
- [Volumes](#volumes)

## Image & Containers
**Images**
```
# List images
docker image ls

# Build an image from the current directory
docker build -t <image-name> .

# Remove an image
docker rmi <image_id>
docker rmi <repository:tag>
```

**Containers**
```
# List running containers
docker ps

# List ALL containers
docker ps -a

# Run a container
docker run <image-name>

# Run a container and remove it after exit
docker run --rm <image-name>

# Run a container with an interactive shell
docker run -it <image-name> sh
```

## Working With Files
```
# Mount current directory into /app inside the container
docker run -v ${PWD}:/app <image-name>

# Set working directory inside the container
docker run -w /app <image-name>
```

## Ports & Networking
```
# Map host port 8000 to container port 5000
docker run -p 8000:5000 <image-name>

# List running containers
docker ps

# View logs for a container
docker logs <container-id>
```

## Cleanup
```
# Remove all stopped containers
docker container prune

# Remove all unused images
docker image prune
```

## Docker Compose
```
# Start all services
docker compose up

# Start all services in detached mode
docker compose up -d

# Stop and remove all services
docker compose down

# Rebuild images and start services
docker compose up --build
```

## Volumes
```
# List all Docker volumes
docker volume ls

# Inspect a specific volume
docker volume inspect <volume-name>

# Explore a volume using a temporary container
docker run --rm -it -v <volume-name>:/data alpine sh
```


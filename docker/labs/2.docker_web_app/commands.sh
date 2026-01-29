# Build docker app
# `.` tells to use dockerfile in this directory
docker build -t flask-app .

# `-p 5000:5000`: Maps port on host to port in container
# Allows us to open our browser to `localhost:5000` and will see app running
docker run -p 5000:5000 flask-app

# Check what ports are in use on host machine
sudo lsof -i -P -n | grep LISTEN

# Because I have stuff running on port 5000 and port 6000, ende rup running flask-app like this:
docker run -p 8000:5000 flask-app

# Remove docker containter
docker rm <container ID>

# Mount volumne of code to avoid having to re-run everytime code change
# `-v${PWD}:/app` : Maps current directory to container
docker run -p 8000:5000 -v${PWD}:/app flask-app

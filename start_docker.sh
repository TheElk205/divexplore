docker volume create mongo_data
docker run -d --name mongodb --net=host --rm -v mongo_data:/data/db mongo:5.0
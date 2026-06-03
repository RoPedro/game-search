CONTAINER_NAME=gamesearch
IMAGE_NAME=gamesearch:latest


docker image rm $IMAGE_NAME --force
docker container rm $CONTAINER_NAME --force

docker build --no-cache . -t $IMAGE_NAME
docker run --name $CONTAINER_NAME -d --memory="512m" --cpus="0.07" $IMAGE_NAME 
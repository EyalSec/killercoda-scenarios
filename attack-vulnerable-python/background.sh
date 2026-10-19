#!/bin/bash
# Start vulnerable-python in a container. It listens on 127.0.0.1:5000 of this
# lab machine only: the app is deliberately insecure, so it is never published
# through the lab's traffic proxy.
set -u
IMAGE=ghcr.io/eyalsec/vulnerable-python:latest
SOURCE=https://github.com/EyalSec/vulnerable-python.git#main
pulled=
for _ in 1 2 3; do docker pull -q "$IMAGE" && pulled=1 && break; sleep 3; done
# If the published image cannot be pulled, build the same app from its public
# source so the lab still starts.
if [ -z "$pulled" ]; then
  echo "Could not pull $IMAGE; building it from $SOURCE instead."
  docker build -q -t "$IMAGE" "$SOURCE"
fi
docker rm -f vulnerable-python >/dev/null 2>&1 || true
docker run -d --name vulnerable-python --restart unless-stopped \
  -p 127.0.0.1:5000:5000 "$IMAGE"
for _ in $(seq 1 60); do
  curl -fs http://127.0.0.1:5000/ >/dev/null && break
  sleep 1
done
touch /tmp/eyalsec-ready

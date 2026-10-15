#!/bin/bash
docker logs vulnerable-python 2>&1 | grep -q 'GET /path?file=../flag.txt'

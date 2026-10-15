# What the app recorded

You read every user's secret, ran commands on the server and read a file
outside the folder the app serves. Here is everything the app wrote down while
that happened:

`docker logs vulnerable-python 2>&1 | tail -15`{{exec}}

A list of requests, each answered `200`. Nothing in it says an attack happened,
and nothing in it says which line of code ran your input. This is ordinary
Python doing exactly what the code asked, which is how most Python services
run today.

Count how many of those requests answered with an error:

`docker logs vulnerable-python 2>&1 | grep -cE '" (4|5)[0-9]{2} ' || true`{{exec}}

Press **Check** to finish.

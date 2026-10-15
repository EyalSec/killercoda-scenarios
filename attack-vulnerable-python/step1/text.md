# Meet the app

The app is running in a container called `vulnerable-python`:

`docker ps --filter name=vulnerable-python`{{exec}}

Each route in the app takes one piece of request data and hands it to one risky
operation. The landing page lists them all:

`curl -s http://127.0.0.1:5000/ | grep -o 'href="/[a-z][^"]*"' | head -20`{{exec}}

Start with an honest request. The `/sqli` route looks a user up by name:

`curl -s "http://127.0.0.1:5000/sqli?name=alice"; echo`{{exec}}

The response shows the SQL query the app ran and the row it found. One user,
as expected. Press **Check** to continue.

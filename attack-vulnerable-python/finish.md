# What the same attacks look like under es-python

You attacked unchanged code, and the only record was a list of successful
requests.

**es-python**, the EyalSec Python runtime, runs the same `app.py` with no code
changes: you type `es-python` where you typed `python`. It follows data that
came from outside (here, the HTTP request) through the program. With its network source
turned on, each of your three attacks would have become an event on your
EyalSec dashboard naming:

- the operation that received your input (the SQL query, the shell command,
  the file open),
- the line of code that performed it,
- the value it received, and where the untrusted part came from.

In **Report** mode the app carries on and the event is recorded. In
**Report and Raise** mode the program gets a `RuntimeError` at that line
instead of running the query, command or file open, so the attack fails rather
than only being logged.

- The app and every route: [EyalSec/vulnerable-python](https://github.com/EyalSec/vulnerable-python)
- How es-python works: [eyalsec.com/docs](https://eyalsec.com/docs)
- See it catch these attacks live: [book a live demo](https://eyalsec.com/contact)

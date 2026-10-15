# Attack a vulnerable Python app

In this lab you will run **vulnerable-python**, a small Flask app written to be
attacked, and break into it three ways: SQL injection, command injection and
path traversal. Each attack takes one `curl` command.

Then comes the part worth remembering. You will look at everything the app
recorded while it was being attacked, and see how little that is.

The app is open source:
[EyalSec/vulnerable-python](https://github.com/EyalSec/vulnerable-python).
It is deliberately insecure, so in this lab it listens on `127.0.0.1` only and
never leaves this throwaway machine.

The terminal on the right is preparing the app. When it says the app is
running, press **Start**.

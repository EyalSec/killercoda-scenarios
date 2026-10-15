# killercoda-scenarios

Hands-on labs from [EyalSec](https://eyalsec.com) that run in your browser on
[Killercoda](https://killercoda.com), each on a throwaway Linux machine of its
own. Nothing to install, nothing left behind.

| Scenario | What you do | Time |
|---|---|---|
| [Attack a vulnerable Python app](attack-vulnerable-python/) | Run [vulnerable-python](https://github.com/EyalSec/vulnerable-python), break into it with SQL injection, command injection and path traversal, then read what the app recorded about it. | 15 minutes |

## How a scenario is laid out

Each folder is one scenario in Killercoda's format: `index.json` lists the
steps, each step is a Markdown page with commands you can click to run, and a
`verify.sh` per step decides when **Check** passes. The intro's
`background.sh` prepares the machine while you read.

The vulnerable app in these labs listens on `127.0.0.1` of the lab machine only
and is never published through the lab's traffic proxy, because it is
deliberately insecure.

## Tested like a learner would use it

`test/run-scenario.py` plays a scenario from start to finish: it runs the
setup, clicks every command on every page (the solutions included) and requires
each step's check to pass. The [Scenarios workflow](.github/workflows/scenarios.yml)
runs it on every change and once a week, so a lab that stops working fails here
first.

```bash
# on a throwaway machine with Docker; Killercoda runs scenarios as root
sudo python3 test/run-scenario.py attack-vulnerable-python
```

## Contributing

Found a step that is unclear or a command that fails? An issue or a pull
request is welcome. To report a security problem in EyalSec itself, email
security@eyalsec.com.

## License

MIT. See [LICENSE](LICENSE).

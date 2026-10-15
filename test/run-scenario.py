#!/usr/bin/env python3
"""Play a Killercoda scenario the way a learner would, outside Killercoda.

For the scenario directory given, it checks that index.json points at files
that exist, runs the intro background script, then for every step runs each
command the learner can click ({{exec}}, inline or fenced, solutions
included) in order, and finally that step's verify script, which must pass.

    sudo python3 test/run-scenario.py attack-vulnerable-python

It runs the commands for real, on this machine, as the current user: use a
throwaway machine or a CI runner.
"""
import json
import os
import re
import subprocess
import sys

FENCED = re.compile(r"```[a-z]*\n(.*?)\n```\{\{exec(?: interrupt)?\}\}", re.S)
INLINE = re.compile(r"`([^`\n]+)`\{\{exec(?: interrupt)?\}\}")


def commands(markdown):
    """Clickable commands in the order they appear on the page."""
    found = [(m.start(), m.group(1)) for m in FENCED.finditer(markdown)]
    spans = [m.span() for m in FENCED.finditer(markdown)]
    for m in INLINE.finditer(markdown):
        if not any(a <= m.start() < b for a, b in spans):
            found.append((m.start(), m.group(1)))
    return [cmd for _, cmd in sorted(found)]


def run(cmd, cwd):
    print(f"$ {cmd}", flush=True)
    res = subprocess.run(["bash", "-c", cmd], cwd=cwd, text=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = res.stdout.strip()
    if out:
        print("  " + out[-800:].replace("\n", "\n  "))
    return res.returncode


def main(scenario):
    with open(os.path.join(scenario, "index.json")) as fh:
        index = json.load(fh)
    details = index["details"]
    referenced = [details["intro"].get(k) for k in ("text", "background", "foreground")]
    referenced += [details["finish"]["text"]]
    for step in details["steps"]:
        referenced += [step["text"], step.get("verify")]
    missing = [p for p in referenced if p and not os.path.isfile(os.path.join(scenario, p))]
    if missing:
        sys.exit(f"index.json references missing files: {missing}")

    if run("bash " + details["intro"]["background"], scenario) != 0:
        sys.exit("background script failed")

    for n, step in enumerate(details["steps"], 1):
        print(f"\n== step {n}: {step['title']}")
        with open(os.path.join(scenario, step["text"])) as fh:
            cmds = commands(fh.read())
        if not cmds:
            sys.exit(f"step {n} has no clickable command")
        for cmd in cmds:
            if run(cmd, "/root" if os.geteuid() == 0 else scenario) != 0:
                sys.exit(f"step {n}: command failed: {cmd}")
        if step.get("verify") and run("bash " + step["verify"], scenario) != 0:
            sys.exit(f"step {n}: verify failed after running the solution")
    print("\nscenario passed")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "attack-vulnerable-python")

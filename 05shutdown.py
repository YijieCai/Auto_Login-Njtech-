import subprocess


def restart_computer():
    subprocess.run(["shutdown", "/r", "/t", "0"])
restart_computer()
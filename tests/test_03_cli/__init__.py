import os
import subprocess


def exec_command(command: str, args=None, timeout=30, cwd=None, env=None) -> tuple:

    if not isinstance(command, str):
        raise ValueError("Parameter 'command' is not string type")

    if not args:
        args = []
    elif not isinstance(args, list):
        raise ValueError("Parameter 'args' is not list type")

    if env:
        env = {**os.environ.copy(), **env}
    else:
        env = os.environ.copy()

    try:
        sp = subprocess.run(
            [command] + args, shell=False, capture_output=True, timeout=timeout, check=False, cwd=cwd, env=env
        )
    except subprocess.TimeoutExpired as e:
        raise TimeoutError(e.output)

    return sp.stdout, sp.stderr, sp.returncode

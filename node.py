from subprocess import Popen, PIPE
import shlex
from bottle import route, run, default_app


@route('/notif/')
def commit():
    handle_notif()
    return "OK"


def handle_notif():
    pass


def run_cmd(cmd, stdin=None):
    if stdin:
        p = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE, stdin=PIPE)
    else:
        p = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(stdin)
    return_code = p.wait()
    return stdout, stderr, return_code


def main():
    run(host='localhost', port=8080)


if __name__ == "__main__":
    main()
else:
    application = default_app()

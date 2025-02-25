from . import exec_command


def test_help_w_arg():

    stdout, stderr, rc = exec_command("tpas-curl-bleeding", args=["--help"])
    assert rc == 0
    assert len(stderr) == 0
    assert 3000 > len(stdout) > 1000


def test_help_no_arg():

    stdout, stderr, rc = exec_command("tpas-curl-bleeding")
    assert rc == 1
    assert len(stderr) == 0
    assert 3000 > len(stdout) > 1000


def test_help_unrelated_args():

    stdout, stderr, rc = exec_command("tpas-curl-bleeding", args=["call", "--url", "https://google.com", "--help"])
    assert rc == 0
    assert len(stderr) == 0
    assert 3000 > len(stdout) > 1000

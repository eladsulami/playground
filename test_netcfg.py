from netcfg import parse_port, build_url


def test_parse_port():
    assert parse_port({"port": "8080"}) == 8080


def test_build_url_default():
    assert build_url("h", {"port": "80"}) == "http://h:80"


def test_build_url_high_port():
    assert build_url("h", {"port": "65535"}) == "http://h:65535"

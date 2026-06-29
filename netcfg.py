def parse_port(cfg):
    return int(cfg["port"])


def build_url(host, cfg):
    return f"http://{host}:{parse_port(cfg)}"

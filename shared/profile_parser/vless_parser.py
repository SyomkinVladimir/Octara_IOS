from urllib.parse import urlsplit, parse_qs, unquote

from shared.models.profile import Profile


def _get_first(query: dict, key: str) -> str:
    return query.get(key, [""])[0]


def parse_vless_url(url: str) -> Profile:
    if not url.startswith("vless://"):
        raise ValueError("Only vless:// URLs are supported")

    parsed = urlsplit(url)

    if "@" not in parsed.netloc:
        raise ValueError("Invalid VLESS URL: missing user info")

    userinfo, hostinfo = parsed.netloc.split("@", 1)

    if ":" not in hostinfo:
        raise ValueError("Invalid VLESS URL: missing port")

    address, port_text = hostinfo.rsplit(":", 1)
    query = parse_qs(parsed.query)

    return Profile(
        uuid=userinfo,
        address=address,
        port=int(port_text),
        remark=unquote(parsed.fragment),
        network=_get_first(query, "type"),
        security=_get_first(query, "security"),
        path=_get_first(query, "path"),
        host=_get_first(query, "host"),
        sni=_get_first(query, "sni"),
        flow=_get_first(query, "flow"),
        fingerprint=_get_first(query, "fp"),
        public_key=_get_first(query, "pbk"),
        short_id=_get_first(query, "sid"),
    )

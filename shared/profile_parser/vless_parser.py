from urllib.parse import urlsplit, parse_qs, unquote

from shared.models.profile import Profile


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
        network=query.get("type", [""])[0],
        security=query.get("security", [""])[0],
        path=query.get("path", [""])[0],
        host=query.get("host", [""])[0],
        sni=query.get("sni", [""])[0],
        flow=query.get("flow", [""])[0],
        fingerprint=query.get("fp", [""])[0],
        public_key=query.get("pbk", [""])[0],
        short_id=query.get("sid", [""])[0],
    )

from urllib.parse import urlparse, unquote

from shared.models.profile import VLESSProfile


def parse_vless_link(link: str) -> VLESSProfile:
    parsed = urlparse(link)

    if parsed.scheme != "vless":
        raise ValueError("Invalid scheme: expected vless://")

    if not parsed.username:
        raise ValueError("Missing UUID in VLESS link")

    if not parsed.hostname:
        raise ValueError("Missing server in VLESS link")

    if not parsed.port:
        raise ValueError("Missing port in VLESS link")

    name = unquote(parsed.fragment) if parsed.fragment else "Unnamed"

    return VLESSProfile(
        raw_link=link,
        name=name,
        server=parsed.hostname,
        port=parsed.port,
        uuid=parsed.username,
    )

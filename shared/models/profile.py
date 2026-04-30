from dataclasses import dataclass


@dataclass
class Profile:
    uuid: str
    address: str
    port: int
    remark: str = ""
    network: str = ""
    security: str = ""
    path: str = ""
    host: str = ""
    sni: str = ""
    flow: str = ""
    fingerprint: str = ""
    public_key: str = ""
    short_id: str = ""
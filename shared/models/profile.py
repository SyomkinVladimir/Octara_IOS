from dataclasses import dataclass


@dataclass
class VLESSProfile:
    raw_link: str
    name: str
    server: str
    port: int
    uuid: str

import json
from dataclasses import asdict, dataclass


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

    def __post_init__(self):
        if not self.uuid:
            raise ValueError("uuid is required")

        if not self.address:
            raise ValueError("address is required")

        if not isinstance(self.port, int):
            raise ValueError("port must be an integer")

        if self.port <= 0 or self.port > 65535:
            raise ValueError("port must be between 1 and 65535")

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)
    
    def save_to_file(self, file_path: str):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(self.to_json())
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    @classmethod
    def load_from_file(cls, file_path: str):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return cls.from_dict(data)      
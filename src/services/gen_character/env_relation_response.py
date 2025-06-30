import json
from dataclasses import dataclass

@dataclass
class EnvRelationResponse:
    related: bool
    word: str | None = None 

    def to_json(self):
        return json.dumps({"related": self.related, "word": self.word})

    @classmethod
    def from_json(cls, json_str: str) -> 'EnvRelationResponse':
        data = json.loads(json_str)
        return cls(**data)
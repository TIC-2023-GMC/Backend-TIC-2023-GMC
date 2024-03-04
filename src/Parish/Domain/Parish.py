from abc import ABC
from typing import Optional

from src.Shared.Model import Model


class Parish(Model, ABC):
    _id: Optional[str]
    label: str
    value: str

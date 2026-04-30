import os
import yaml
from pathlib import Path


DEFAULT_PATH = Path.home() / ".mqtrace" / "profiles.yml"


def load_profiles(path: str | None = None) -> dict:
    file_path = Path(path) if path else DEFAULT_PATH

    if not file_path.exists():
        return {}

    with open(file_path, "r") as f:
        data = yaml.safe_load(f) or {}

    return data.get("profiles", {})
from pathlib import Path

from mqtrace.profiles.loader import load_profiles


def test_load_profiles_from_yaml(tmp_path: Path):
    profiles_file = tmp_path / "profiles.yml"
    profiles_file.write_text(
        """
profiles:
  local-dev:
    type: static
    host: localhost
    port: 1414
    queue_manager: QM1
"""
    )

    profiles = load_profiles(str(profiles_file))

    assert "local-dev" in profiles
    assert profiles["local-dev"]["type"] == "static"
    assert profiles["local-dev"]["queue_manager"] == "QM1"


def test_load_profiles_returns_empty_when_file_missing(tmp_path: Path):
    missing_file = tmp_path / "missing.yml"

    profiles = load_profiles(str(missing_file))

    assert profiles == {}
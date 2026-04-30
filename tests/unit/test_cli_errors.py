import mqtrace.profiles.loader as loader
from mqtrace.profiles.resolver import get_profile


def test_profile_not_found_error_shows_available_profiles(tmp_path):
    file = tmp_path / "profiles.yml"
    file.write_text(
        """
profiles:
  local-dev:
    type: static
"""
    )

    loader.DEFAULT_PATH = file

    try:
        get_profile("missing")
        assert False
    except ValueError as e:
        assert "Profile 'missing' not found" in str(e)
        assert "local-dev" in str(e)
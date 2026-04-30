from mqtrace.profiles.loader import load_profiles


def get_profile(name: str) -> dict:
    profiles = load_profiles()

    if name not in profiles:
        raise ValueError(f"Profile '{name}' not found")

    return profiles[name]
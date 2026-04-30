from mqtrace.profiles.loader import load_profiles


def get_profile(name: str) -> dict:
    profiles = load_profiles()

    if name not in profiles:
        available = ", ".join(profiles.keys()) or "none"
        raise ValueError(f"Profile '{name}' not found. Available: {available}")

    return profiles[name]
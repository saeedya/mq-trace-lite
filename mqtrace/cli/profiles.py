import typer
from rich.console import Console
from rich.table import Table
from mqtrace.profiles.loader import load_profiles

console = Console()


def profiles_list():
    """List configured profiles."""

    profiles = load_profiles()

    if not profiles:
        console.print("[red]No profiles found[/red]")
        return

    table = Table(title="Profiles")

    table.add_column("Name")
    table.add_column("Type")
    table.add_column("Namespace")
    table.add_column("Queue Manager")

    for name, cfg in profiles.items():
        table.add_row(
            name,
            cfg.get("type", "-"),
            cfg.get("namespace", "-"),
            cfg.get("queue_manager", "-"),
        )

    console.print(table)
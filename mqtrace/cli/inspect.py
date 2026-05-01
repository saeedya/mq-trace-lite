import typer
from rich.console import Console
from rich.table import Table
from mqtrace.core.messages import get_messages
from mqtrace.profiles.resolver import get_profile

console = Console()


def inspect(
    profile: str = typer.Option(..., help="Profile name"),
    queue: str = typer.Option(..., help="Queue name"),
    correlation_id: str = typer.Option(None, help="Filter by correlation ID"),
    limit: int = typer.Option(5, help="Number of messages to show"),
):
    """Inspect messages from a queue."""

    if not queue:
        console.print("[red]Queue is required[/red]")
        raise typer.Exit(1)

    try:
        cfg = get_profile(profile)
    except ValueError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(1)

    console.print(f"[bold green]Profile:[/bold green] {profile}")
    console.print(f"[bold green]Queue:[/bold green] {queue}")

    messages = get_messages(cfg, queue, correlation_id, limit)

    table = Table(title="Messages")
    table.add_column("Message ID")
    table.add_column("Correlation ID")
    table.add_column("Queue")
    table.add_column("Status")
    table.add_column("Host")
    table.add_column("Timestamp")
    table.add_column("Size")
    table.add_column("Payload")

    for msg in messages:
        table.add_row(
            msg["message_id"],
            msg["correlation_id"],
            msg["queue"],
            msg["status"],
            msg.get("host", "-"),
            msg["timestamp"],
            str(msg["size"]),
            msg.get("payload_preview", "-"),
        )

    console.print(table)
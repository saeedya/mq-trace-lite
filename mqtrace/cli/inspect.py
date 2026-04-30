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

    cfg = get_profile(profile)

    console.print(f"[bold green]Profile:[/bold green] {profile}")
    console.print(f"[bold green]Queue:[/bold green] {queue}")

    messages = get_messages(queue, correlation_id, limit)

    table = Table(title="Messages")

    table.add_column("Message ID")
    table.add_column("Correlation ID")
    table.add_column("Queue")
    table.add_column("Status")

    for msg in messages:
        table.add_row(
            msg["message_id"],
            msg["correlation_id"],
            msg["queue"],
            msg["status"],
        )

    console.print(table)
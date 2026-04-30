import typer
from rich.console import Console
from rich.table import Table
from mqtrace.core.messages import get_messages

console = Console()


def inspect(
    queue: str = typer.Option(..., help="Queue name"),
    correlation_id: str = typer.Option(None, help="Filter by correlation ID"),
    limit: int = typer.Option(5, help="Number of messages to show"),
):
    """Inspect messages from a queue."""

    console.print(f"[bold green]Inspecting queue:[/bold green] {queue}")

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
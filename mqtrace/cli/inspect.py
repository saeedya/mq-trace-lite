import typer
from rich.console import Console
from rich.table import Table

console = Console()


def inspect(
    queue: str = typer.Option(..., help="Queue name"),
    correlation_id: str = typer.Option(None, help="Filter by correlation ID"),
    limit: int = typer.Option(5, help="Number of messages to show"),
):
    """Inspect messages from a queue (fake data for now)."""

    console.print(f"[bold green]Inspecting queue:[/bold green] {queue}")

    if correlation_id:
        console.print(f"[yellow]Filter:[/yellow] correlation_id={correlation_id}")

    table = Table(title="Messages")

    table.add_column("Message ID")
    table.add_column("Correlation ID")
    table.add_column("Queue")
    table.add_column("Status")

    # fake data
    for i in range(limit):
        table.add_row(
            f"msg-{i}",
            correlation_id or f"corr-{i}",
            queue,
            "READY",
        )

    console.print(table)
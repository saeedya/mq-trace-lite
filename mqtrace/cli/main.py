import typer
from rich.console import Console
from mqtrace.cli.inspect import inspect

app = typer.Typer(
    help="CLI-first IBM MQ debugging and incident tool.",
    no_args_is_help=True,
)

console = Console()


@app.callback()
def callback() -> None:
    """MQ Trace Lite CLI."""
    pass


@app.command()
def version() -> None:
    """Show MQ Trace Lite version."""
    console.print("mq-trace-lite version 0.1.0")


app.command()(inspect)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
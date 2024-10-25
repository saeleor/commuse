"""Command-line interface for Commuse."""
import typer
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from . import __version__
from .git import get_staged_changes
from .generator import generate_commit_message

app = typer.Typer(
    name="commuse",
    help="AI-powered semantic commit message generator",
    add_completion=False,
)
console = Console()

def version_callback(value: bool):
    """Show the version and exit."""
    if value:
        console.print(f"Commuse version: {__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
):
    """Commuse - AI-powered semantic commit message generator."""
    pass

@app.command()
def generate():
    """Generate a semantic commit message based on staged changes."""
    with console.status("Reading staged changes..."):
        diff = get_staged_changes()

    if not diff:
        console.print("[red]No staged changes found.[/red]")
        raise typer.Exit(1)
    
    with console.status("Generating commit message..."):
        try:
            message = generate_commit_message(diff)
            
            # Display the results
            console.print("\n[bold green]Suggested commit message:[/bold green]")
            console.print(Panel(message.title, title="Title"))
            
            if message.description:
                console.print(Panel(
                    Markdown(message.description),
                    title="Description"
                ))
        except Exception as e:
            console.print(f"[red]Error generating commit message: {str(e)}[/red]")
            raise typer.Exit(1)

if __name__ == "__main__":
    app()


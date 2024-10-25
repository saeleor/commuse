import subprocess
import typer
from rich.console import Console
from rich import print as rprint
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

app = typer.Typer()
console = Console()

def get_staged_changes() -> str:
    """Get the staged changes from git."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--cached'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError:
        raise typer.Exit("No staged changes found or not in a git repository")

def generate_commit_message(diff: str) -> str:
    """Generate a semantic commit message using OpenAI"""
    
    prompt = f"""Given the following git diff, generate a semantic commit message.
# The message should follow the conventional commits specification: type(scope): description
# The type should be one of: feat, fix, docs, style, refactor, perf, test, chore
# Keep the message concise and under 70 characters.

# Git diff:
# {diff}

# Generate only the commit message, nothing else.
# """

    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"{prompt}"},
        ]
    )

    return completion.choices[0].message.content

@app.command()
def main():
  """Generate a semantic commit message based on staged changes."""
  with console.status("Reading staged changes..."):
    diff = get_staged_changes()

  if not diff:
    rprint("[red]No staged changes found.[/red]")
    raise typer.Exit(1)
  
  with console.status("Generating commit message..."):
    try:
      message = generate_commit_message(diff)
      rprint(f"\n{message}")
    except Exception as e:
      rprint(f"[red]Error generating commit message: {str(e)}[/red]")
      raise typer.Exit(1)
    
if __name__ == "__main__":
  app()

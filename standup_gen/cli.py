import click
from git_utils import get_recent_commits
from openai_client import generate_standup
from utils import copy_to_clipboard
from formatter import format_standup_output, format_clipboard_message


@click.group()
def cli():
    """Standup Generator CLI - Generate daily standup updates from Git commits."""
    pass


@cli.command()
@click.option('--since', default=24, help='Number of hours to look back for commits (default: 24)')
def generate(since):
    """Generate a standup update from recent Git commits."""
    
    # Get recent commits
    commits = get_recent_commits(since_hours=since)
    
    # Prompt user for additional notes
    notes = click.prompt("Anything else to include?", default="", show_default=False)
    
    # Generate standup using AI
    standup_update = generate_standup(commits, notes)
    
    # Format and print the standup
    formatted_output = format_standup_output(standup_update)
    print(formatted_output)
    
    # Copy to clipboard and show result
    clipboard_success = copy_to_clipboard(standup_update)
    print(format_clipboard_message(clipboard_success))


if __name__ == '__main__':
    cli()
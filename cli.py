import click
from git_reader import get_recent_commits
from agent import generate_standup
from utils import copy_to_clipboard


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
    
    # Print the generated standup with clean formatting
    print("\n" + "=" * 60)
    print("📋 YOUR STANDUP UPDATE")
    print("=" * 60)
    print()
    print(standup_update)
    print()
    print("=" * 60)
    
    # Copy to clipboard
    if copy_to_clipboard(standup_update):
        print("✅ Standup copied to clipboard!")
    else:
        print("⚠️  Could not copy to clipboard")


if __name__ == '__main__':
    cli()
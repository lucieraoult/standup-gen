import subprocess
from datetime import datetime, timedelta
from typing import List


def get_recent_commits(since_hours: int = 24) -> List[str]:
    """
    Get commit messages from the last N hours.
    
    Args:
        since_hours: Number of hours to look back for commits (default: 24)
        
    Returns:
        List of clean commit messages
    """
    since_time = datetime.now() - timedelta(hours=since_hours)
    since_str = since_time.isoformat()

    try:
        # Run git log command to get commits since the specified time
        result = subprocess.run(
            ["git", "log", f"--since={since_str}", "--pretty=format:%s"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Split by newlines and filter out empty lines
        commit_messages = [
            line.strip() 
            for line in result.stdout.split('\n') 
            if line.strip()
        ]
        
        return commit_messages
        
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {e}")
        return []
    except FileNotFoundError:
        print("Git is not installed or not in PATH")
        return []


if __name__ == "__main__":
    commits = get_recent_commits()
    
    if commits:
        print(f"Found {len(commits)} commits in the last 24 hours:")
        print("-" * 50)
        for i, commit in enumerate(commits, 1):
            print(f"{i}. {commit}")
    else:
        print("No commits found in the last 24 hours")
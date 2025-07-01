# standup-gen

A Python CLI tool that automatically generates daily standup updates using your Git commit history and OpenAI's API.

## What it does

standup-gen helps software engineers quickly create professional standup updates by:

- 📝 Analyzing your recent Git commits 
- 🤖 Using OpenAI's API to generate a structured update
- 📋 Formatting it into a clear 3-section standup
- 📎 Automatically copying the result to your clipboard

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd standup-gen
```

2. Install required dependencies:
```bash
pip install click openai python-dotenv pyperclip
```

3. Set up your OpenAI API key:
```bash
# Create a .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

## Usage

Generate a standup update from the last 24 hours:
```bash
python cli.py generate
```

Specify a custom time range (in hours):
```bash
python cli.py generate --since 48
```

## Demo Example

```bash
$ python cli.py generate
Anything else to include? []: Working on the new user dashboard, might need help with API rate limiting

============================================================
📋 YOUR STANDUP UPDATE
============================================================

🛠 Yesterday
- Fixed user authentication bug in login flow
- Added pagination to user dashboard
- Updated API documentation for new endpoints
- Refactored database connection handling

📌 Today
- Continue work on user dashboard improvements
- Investigate API rate limiting solutions
- Review and merge pending pull requests

⚠️ Blockers
- Need assistance with API rate limiting implementation

============================================================
✅ Standup copied to clipboard!
```

## Requirements

- Python 3.7+
- Git repository (the tool analyzes your commit history)
- OpenAI API key
- Dependencies: `click`, `openai`, `python-dotenv`, `pyperclip`

## Configuration

Create a `.env` file in the project directory with your OpenAI API key:
```
OPENAI_API_KEY=sk-your-api-key-here
```

## How it works

1. **Git Analysis**: Scans your Git commit messages from the specified time period
2. **User Input**: Prompts for additional notes, blockers, or plans
3. **AI Generation**: Sends commit data and notes to OpenAI's API with a specialized prompt
4. **Formatting**: Returns a structured standup with Yesterday/Today/Blockers sections
5. **Clipboard**: Automatically copies the result for easy pasting into Slack, Teams, etc.

## Tips

- Run it from any Git repository directory
- Use `--since` to adjust the time window for commits
- Add notes about blockers, plans, or context that isn't in your commits
- The generated update is automatically copied to your clipboard for easy sharing
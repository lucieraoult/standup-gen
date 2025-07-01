import os
from openai import OpenAI
from dotenv import load_dotenv


def generate_standup(commits: list[str], notes: str) -> str:
    """
    Generate a formatted standup update using OpenAI based on Git commits and notes.
    
    Args:
        commits: List of commit messages from recent work
        notes: Additional notes from the user
        
    Returns:
        Formatted standup update string
    """
    load_dotenv()
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 
    
    # Prepare the prompt
    commits_text = "\n".join([f"- {commit}" for commit in commits]) if commits else "No commits found"
    notes_text = notes.strip() if notes.strip() else "No additional notes"
    
    prompt = f"""You are helping a software engineer generate their daily standup update.

Based on the following Git commits and notes, create a clear, professional, and informal standup update in **this exact format**:

🛠 Yesterday
- Bullet points for what was accomplished

📌 Today
- Bullet points for what's planned next

⚠️ Blockers
- Any blockers or "None"

Git commits from yesterday:
{commits_text}

Additional notes:
{notes_text}

Keep it concise, use bullet points where appropriate, and maintain a conversational but professional tone. Focus on the actual work done rather than just listing commit messages."""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        return f"Error generating standup: {str(e)}"


if __name__ == "__main__":
    # Sample data for testing
    sample_commits = [
        "Fix user authentication bug in login flow",
        "Add pagination to user dashboard",
        "Update API documentation for new endpoints",
        "Refactor database connection handling"
    ]
    
    sample_notes = "Working on the new feature branch, might need help with the database migration"
    
    result = generate_standup(sample_commits, sample_notes)
    print("Generated Standup Update:")
    print("=" * 50)
    print(result)
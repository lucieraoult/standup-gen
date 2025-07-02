def format_standup_output(standup_content: str) -> str:
    """
    Format the standup output with clean styling and spacing.
    
    Args:
        standup_content: The generated standup content from OpenAI
        
    Returns:
        Formatted string ready for display
    """
    header = "=" * 60
    title = "📋 YOUR STANDUP UPDATE"
    
    formatted_output = f"\n{header}\n{title}\n{header}\n\n{standup_content}\n\n{header}"
    
    return formatted_output


def format_clipboard_message(success: bool) -> str:
    """
    Format the clipboard copy result message.
    
    Args:
        success: Whether clipboard copy was successful
        
    Returns:
        Formatted success or error message
    """
    if success:
        return "✅ Standup copied to clipboard!"
    else:
        return "⚠️  Could not copy to clipboard"
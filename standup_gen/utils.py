def copy_to_clipboard(text: str) -> bool:
    """
    Copy text to the system clipboard using pyperclip.
    
    Args:
        text: The text to copy to clipboard
        
    Returns:
        True if successful, False otherwise
    """
    try:
        import pyperclip
        pyperclip.copy(text)
        return True
    except ImportError:
        print("⚠️  pyperclip not installed. Install with: pip install pyperclip")
        return False
    except Exception as e:
        print(f"⚠️  Failed to copy to clipboard: {e}")
        return False
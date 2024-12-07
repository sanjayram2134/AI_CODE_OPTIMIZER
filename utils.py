import base64
from pygments.lexers import guess_lexer

def detect_language(code):
    """
    Detects the programming language of the given code snippet.
    """
    try:
        lexer = guess_lexer(code)
        return lexer.name
    except:
        return "unknown"

def download_link(text, filename):
    """
    Generates a download link for the provided text.
    """
    b64 = base64.b64encode(text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">Download Suggestions</a>'
    return href

from urllib.parse import urlparse, parse_qs
from typing import Tuple

def is_valid_youtube_video(url: str) -> Tuple[bool, str]:
    """
    Validates a YouTube video URL.
    Returns a tuple (is_valid, error_message).
    """
    try:
        parsed = urlparse(url)
        if parsed.netloc not in ["www.youtube.com", "youtube.com", "youtu.be"]:
            return False, "Only YouTube video URLs are supported."

        if "playlist" in parsed.path or "list=" in url:
            return False, "This appears to be a playlist URL. Please use the 'Download Playlist' option."

        if parsed.netloc == "youtu.be":
            return True, ""

        query = parse_qs(parsed.query)
        if "v" in query:
            return True, ""

        return False, "Invalid YouTube video URL."

    except Exception:
        return False, "Malformed URL."

def is_valid_youtube_playlist(url: str) -> Tuple[bool, str]:
    """
    Validates a YouTube playlist URL.
    Returns a tuple (is_valid, error_message).
    """
    try:
        parsed = urlparse(url)
        if parsed.netloc not in ["www.youtube.com", "youtube.com"]:
            return False, "Only YouTube playlist URLs are supported."

        query = parse_qs(parsed.query)
        if "list" in query:
            return True, ""

        return False, "This does not appear to be a valid playlist URL."

    except Exception:
        return False, "Malformed URL."
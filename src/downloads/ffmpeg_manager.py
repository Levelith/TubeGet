import os

def get_ffmpeg_path():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ffmpeg_path = os.path.join(base_dir, "dependencies", "ffmpeg.exe")
    if os.path.exists(ffmpeg_path):
        return ffmpeg_path
    else:
        return None
    
def is_ffmpeg_available():
    return get_ffmpeg_path() is not None
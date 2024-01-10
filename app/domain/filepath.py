"""Filepath helpers."""
import os
from pathlib import Path


def pwd() -> Path:
    """Get current working directory.
    
    Returns:
        str: Current working directory
    """
    return Path().resolve()


def to_pwd_path(path: str | Path) -> Path:
    """Convert relative path with respect to current working directory.
    
    E.g. 'path' -> '$PWD'/'path'
    
    Arguments:
        path -- str: Relative path
    
    Returns:
        Path: Absolute path
    """
    if os.path.isabs(path):
        return Path(path)
    
    return pwd() / path

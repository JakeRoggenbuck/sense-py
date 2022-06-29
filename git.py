from pathlib import Path


def has_git(path: str) -> bool:
    return (Path(path) / ".git").exists()

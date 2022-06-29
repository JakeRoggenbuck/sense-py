from pathlib import Path


def has_git(path: str) -> bool:
    return (Path(path) / ".git").exists()


def is_local_git(path: str) -> bool:
    if not has_git(path):
        return False

    with open(path + "/.git/config") as file:
        content = file.read()

    if "url" not in content:
        return False

    return True

from pathlib import Path
from enum import Enum


class Lang(Enum):
    PYTHON = 0
    RUST = 1
    JAVA = 2
    JS = 3
    GO = 4
    NONE = 5


def has_sub_file(path: str, sub: str) -> bool:
    if (Path(path) / sub).exists():
        return True

    return False


def get_lang(path: str) -> Lang:
    if has_sub_file(path, "/setup.py"):
        return Lang.PYTHON
    elif has_sub_file(path, "/package.json"):
        return Lang.JS
    elif has_sub_file(path, "/Cargo.toml"):
        return Lang.RUST
    elif has_sub_file(path, "/pom.xml"):
        return Lang.JAVA
    elif has_sub_file(path, "/go.mod"):
        return Lang.GO

    return Lang.NONE

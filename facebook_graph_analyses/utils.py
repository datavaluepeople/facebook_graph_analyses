"""Utils."""
import pathlib


def relative_path(path: str, file_path: str) -> pathlib.Path:
    """Form path of the relative path from __file__'s directory."""
    return (pathlib.Path(file_path).parent.absolute() / path).absolute()

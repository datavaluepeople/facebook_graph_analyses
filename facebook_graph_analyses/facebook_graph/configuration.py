"""Facebook graph configuration."""
import re
from dataclasses import dataclass

import requests


DEFAULT_API_VERSION = "v15.0"


@dataclass
class FacebookGraphConfig:
    """Configuration of Facebook graph requests."""

    api_version: str
    access_token: str
    session: requests.Session


def create_config(
    access_token: str,
    api_version: str = DEFAULT_API_VERSION,
    session: requests.Session = requests.Session(),
) -> FacebookGraphConfig:
    """Create a FacebookGraphConfig."""
    api_pattern = re.compile(r"^v\d+\.\d+$")
    if not re.match(api_pattern, api_version):
        raise ValueError(f"API version is not correctly {api_version}")
    if not access_token:
        raise ValueError(f"Access Token must be given: {access_token}")
    if not isinstance(session, requests.Session):
        raise ValueError(
            f"Session must be a requests.session: {type(session)} was given"
        )
    return FacebookGraphConfig(
        api_version=api_version, access_token=access_token, session=session
    )

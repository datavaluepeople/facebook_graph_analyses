"""Requests for facebook_graph."""
from typing import Any, Dict

from facebook_graph_analyses.facebook_graph import configuration


FACEBOOK_GRAPH_URL = "https://graph.facebook.com/"


def get(
    cfg: configuration.FacebookGraphConfig, endpoint: str, params: Dict[Any, Any] = {}
):
    """Make a get request for the facebook API.

    Args:
        cfg: configuration.FacebookGraphConfig
        endpoint: facebook API endpoint with no "/" prefix.
        params: parameters for the endpoint
    returns:
        Dict of the response.
    """
    get_url = f"{FACEBOOK_GRAPH_URL}{cfg.api_version}/{endpoint}"

    if not type(params) is dict:
        raise ValueError(f"Params must be a dictionary. {type(params)} was given")

    params["access_token"] = cfg.access_token
    response = cfg.session.request(
        "GET",
        get_url,
        params=params,
    )

    headers = response.headers
    content_type = headers["content-type"]
    if "json" in content_type:
        return response.json()

    unsupported_err_msg = (
        f"Unsupported content-type returned from API: {content_type}."
        "Consider using a different API endpoint or requesting new"
        " functionality in repo."
    )
    raise RuntimeError(unsupported_err_msg)

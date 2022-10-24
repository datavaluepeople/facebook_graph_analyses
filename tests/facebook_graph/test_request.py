"""Test request for facebook graph."""
from typing import Any, Dict

import mock
import pytest
import requests

from facebook_graph_analyses.facebook_graph import configuration, request


def test_successful_get():
    """Test a successful get."""
    access_token = "access_token"
    api_version = "v1.0"
    mock_session = mock.MagicMock(spec=requests.Session)
    mock_session.request.return_value.headers = {"content-type": "json"}
    endpoint = "me"
    params: Dict[str, Any] = {"fields": ["1"]}
    cfg = configuration.FacebookGraphConfig(
        access_token=access_token,
        api_version=api_version,
        session=mock_session,
    )
    result = request.get(cfg, endpoint, params)
    expected_params = params.copy()
    expected_params["access_token"] = access_token
    mock_session.request.assert_called_once_with(
        "GET",
        f"{request.FACEBOOK_GRAPH_URL}{api_version}/{endpoint}",
        params=expected_params,
    )

    assert result == mock_session.request().json()


def test_successful_get_unsupported_content_type():
    """Test a successful get."""
    access_token = "access_token"
    api_version = "v1.0"
    mock_session = mock.MagicMock(spec=requests.Session)
    unsupported_content_type = "content-unsupported"
    mock_session.request.return_value.headers = {
        "content-type": unsupported_content_type
    }
    endpoint = "me"
    params: Dict[str, Any] = {"fields": ["1"]}
    cfg = configuration.FacebookGraphConfig(
        access_token=access_token,
        api_version=api_version,
        session=mock_session,
    )
    with pytest.raises(RuntimeError) as err:
        _ = request.get(cfg, endpoint, params)
        expected_params = params.copy()
        expected_params["access_token"] = access_token
        mock_session.request.assert_called_once_with(
            "GET",
            f"{request.FACEBOOK_GRAPH_URL}{api_version}/{endpoint}",
            params=expected_params,
        )

        assert "Unsupported content-type" in str(err)
        assert unsupported_content_type in str(err)

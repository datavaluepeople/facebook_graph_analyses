"""Test facebook_graph configuration."""
import pytest
import requests

from facebook_graph_analyses.facebook_graph import configuration


def test_create_config_default():
    """Test create config for default."""
    access_token = "access_token"
    facebook_graph_cfg = configuration.create_config(access_token=access_token)
    assert isinstance(facebook_graph_cfg, configuration.FacebookGraphConfig)
    assert facebook_graph_cfg.access_token == access_token
    assert facebook_graph_cfg.api_version == configuration.DEFAULT_API_VERSION
    assert isinstance(facebook_graph_cfg.session, requests.Session)


def test_create_config_errors_access_token():
    """Test create config for invalid access token."""
    access_token = ""
    with pytest.raises(ValueError) as err:
        _ = configuration.create_config(access_token=access_token)
        assert "Access Token" in str(err)


def test_create_config_errors_session():
    """Test create config for default."""
    access_token = "access_token"
    session = "session"
    with pytest.raises(ValueError) as err:
        _ = configuration.create_config(
            access_token=access_token, session=session  # type: ignore
        )
        assert "Session" in str(err)
        assert "String was given" in str(err)


def test_create_config_with_params():
    """Test create config for a given api version and session."""
    api_version = "v14.0"
    access_token = "access_token"
    session = requests.Session()
    facebook_graph_cfg = configuration.create_config(
        access_token=access_token, api_version=api_version, session=session
    )
    assert isinstance(facebook_graph_cfg, configuration.FacebookGraphConfig)
    assert facebook_graph_cfg.access_token == access_token
    assert facebook_graph_cfg.api_version == api_version
    assert facebook_graph_cfg.session == session


@pytest.mark.parametrize("invalid_api_version", ["1", "v1", "14.0", "f1"])
def test_create_config_errors_api_version(invalid_api_version):
    """Test create config for default."""
    access_token = "access_token"
    with pytest.raises(ValueError) as err:
        _ = configuration.create_config(
            access_token=access_token,
            api_version=invalid_api_version,
        )
        assert "API version" in str(err)
        assert invalid_api_version in str(err)

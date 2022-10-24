"""Test facebook_graph configuration."""
import pytest

from facebook_graph_analyses.facebook_graph import configuration


def test_create_config_default():
    """Test create config for default."""
    access_token = "access_token"
    facebook_graph_cfg = configuration.create_config(access_token=access_token)
    assert isinstance(facebook_graph_cfg, configuration.FacebookGraphConfig)
    assert facebook_graph_cfg.access_token == access_token
    assert facebook_graph_cfg.api_version == configuration.DEFAULT_API_VERSION


def test_create_config_errors_access_token():
    """Test create config for invalid access token."""
    access_token = ""
    with pytest.raises(ValueError) as err:
        _ = configuration.create_config(access_token=access_token)
        assert "Access Token" in str(err)


def test_create_config_with_api_version():
    """Test create config for a given api version."""
    api_version = "v14.0"
    access_token = "access_token"
    facebook_graph_cfg = configuration.create_config(
        access_token=access_token,
        api_version=api_version,
    )
    assert isinstance(facebook_graph_cfg, configuration.FacebookGraphConfig)
    assert facebook_graph_cfg.access_token == access_token
    assert facebook_graph_cfg.api_version == api_version


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

"""Tests for wordcloud_for_pages."""
import os

from click.testing import CliRunner

from facebook_graph_analyses import cli, utils


def test_wordcloud_for_pages(tmp_path):
    """Test wordcloud for pages."""
    input_data_dir = tmp_path / "input_data"
    input_data_dir.mkdir()
    output_png_path = "output_wordcloud.png"
    access_token = "access_token"
    runner = CliRunner()
    input_data_file = utils.relative_path("./input_data/list_of_pages.csv", __file__)
    with runner.isolated_filesystem(tmp_path):
        assert os.path.exists(input_data_file)
        result = runner.invoke(
            cli.main_group.main_group,
            [
                "wordcloud-for-pages",
                "run",
                str(input_data_file),
                output_png_path,
                access_token,
            ],
        )
        assert result.exit_code == 0

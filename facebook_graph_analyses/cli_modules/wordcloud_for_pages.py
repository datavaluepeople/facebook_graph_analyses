"""Wordcloud for pages CLI Interface."""
import click

from facebook_graph_analyses.cli_modules import main_group


@main_group.main_group.group()
def wordcloud_for_pages():
    """Wordcloud for pages."""


@wordcloud_for_pages.command("run")
@click.argument("list_of_pages_path", type=click.Path(exists=True))
@click.argument("output_wordcloud_path", type=click.Path())
@click.argument("access_token", type=click.STRING)
def run(list_of_pages_path, output_wordcloud_path, access_token):
    """Run wordcloud for the pages analysis.

    LIST_OF_PAGES_PATH: a path to a csv that holds the list of pages to analyse
    OUTPUT_WORDCLOUD_PATH: a path to `.png` that will be output by the analyse
    ACCESS_TOKEN: access token to be used for requests to facebook graph API
    """
    click.echo("Starting wordcloud for pages analysis")

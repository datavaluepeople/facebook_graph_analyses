"""CLI click interface."""

# Importing the non used cli_modules
# So that the CLI is correctly initialised
from facebook_graph_analyses.cli_modules import (
    main_group,
    wordcloud_for_pages,
)  # noqa: F401


if __name__ == "__main__":
    main_group.main_group()

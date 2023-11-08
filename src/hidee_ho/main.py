from pathlib import Path

import click

from hidee_ho import maps


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument("states", nargs=-1)
@click.option("--output", "-o", help="filename to create", type=click.Path())
@click.option(
    "--force", "-f", default=False, is_flag=True, help="overwrite file if it exists"
)
def cli(states: list[str], output: str, force=False):
    """
    This function generates a map based on the given states.

    Parameters:
    - states: A list of states to include in the map.

    Optional Parameters:
    - output: The filename to create for the map.
    - force: If True, overwrite the file if it exists.

    Returns:
    None
    """
    # Validate the states argument
    for state in states:
        if not maps.valid_state(state):
            raise ValueError(f"Invalid state name: {state}")

    my_map = maps.mapper(states)

    _output = Path(output)

    if not force and _output.exists():
        click.Abort(f"{_output} already exists, use the --force flag to overwrite")

    my_map.write_html(output) if output else my_map.show()


if __name__ == "__main__":
    cli()

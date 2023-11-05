from pathlib import Path

import click

from hidee_ho.maps import mapper


@click.command()
@click.option("--states", "-s", help="list of states to color")
@click.option("--output", "-o", help="filename to create")
@click.option(
    "--force", "-f", default=False, is_flag=True, help="overwrite file if it exists"
)
def cli(states: list[str], output: str, force=False):
    my_map = mapper(states)

    if output:
        _output = Path(output)

        if not force and _output.exists():
            raise FileExistsError(
                f"{_output} already exists, use the --force flag to overwrite"
            )

        my_map.write_html(output)
    else:
        my_map.show()


if __name__ == "__main__":
    cli()

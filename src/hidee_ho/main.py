import click

from hidee_ho.maps import mapper


@click.command()
@click.option("--states", "-s", help="list of states to color")
@click.option("--output", "-o", help="filename to create")
def cli(states: list[str], output):
    my_map = mapper(states)
    my_map.output(output)


if __name__ == "__main__":
    cli()

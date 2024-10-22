import click
from boss import generate

@click.group()
def cli():
    """MODULE BOSS

    This module is in charge of generating new reports from the boss report.
    """
    pass

@cli.command(help="Create the total clients report by state and bras")
def clients():
    generate.clients_by_BRAS_and_state()

if __name__ == "__main__":
    try:
        cli()
    except Exception as error:
        click.echo(error)

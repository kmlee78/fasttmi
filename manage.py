import click
from alembic import command
from alembic.config import Config

alembic_cfg = Config("./alembic.ini")


@click.group()
def cli():
    ...


@click.command(help="Show current revision")
def current():
    command.current(alembic_cfg)


@click.command(help="Downgrade to previous revision")
def downgrade():
    command.downgrade(alembic_cfg, "-1")


@click.command(help="Upgrade to next revision")
def upgrade():
    command.upgrade(alembic_cfg, "+1")


@click.command(help="Show migration history")
def history():
    command.history(alembic_cfg)


@click.command(help="Create new migration file")
def makemigrations():
    command.revision(alembic_cfg, autogenerate=True)


cli.add_command(current)
cli.add_command(downgrade)
cli.add_command(upgrade)
cli.add_command(history)
cli.add_command(makemigrations)

if __name__ == "__main__":
    cli()

import click
from cli.api_usage import plot_requests_hist
from cli.users import plot_users_hist

from flask import current_app as app
from flask.cli import with_appcontext

F_PLOTS = {
    "api-usage-requests-hist": plot_requests_hist,
    "users-hist": plot_users_hist
}


@click.group()
def plots():
    """Performs operations with Plotly backend"""
    pass


@plots.command()
@click.option(
    "-s",
    "--select",
    type=click.Choice(["all"] + list(F_PLOTS.keys()), case_sensitive=False),
    default="all",
    help="Generate a plot for a given function. By default, will generate all plots."
)
@click.pass_context
def generate(ctx, select):
    if select == "all":
        for key, f in F_PLOTS.items():
            click.secho(f"Generating plot: {key}")
            ctx.invoke(f)
    else:
        f = F_PLOTS[select]
        ctx.invoke(f)


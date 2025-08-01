"""Main module for the PDM slim reproduction case."""

import click
import requests


@click.command()
def hello():
    """Simple function that uses our dependencies."""
    response = requests.get("https://httpbin.org/json")
    click.echo(f"Status: {response.status_code}")
    click.echo("Hello from PDM slim repro!")


if __name__ == "__main__":
    hello()
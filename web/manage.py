import typer
import os

from src import __version__

app = typer.Typer()

def version_callback(value: bool):
    if not value:
        return
    typer.echo(__version__)
    raise typer.Exit()

@app.callback()
def main(
    version: bool = typer.Option(None, callback=version_callback, is_eager=True, help="show current version"),
):
    pass


@app.command()
def lint():
    """
    Run black formatter ( soon tm )
    """
    print("run linter later")


@app.command()
def serve():
    """
    Run the backend server locally
    """
    os.system("uvicorn src.main:app")


if __name__ == "__main__":
    app()

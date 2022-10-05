import click
from tasks import scrape


@click.command(context_settings=dict(allow_extra_args=True))
@click.option("--task", envvar="TASK")
@click.option("--data_name", envvar="DATA_NAME")
def run(task: str, data_name: str = None):
    if task == "scrape":
        scrape.run(data_name)


if __name__ == "__main__":
    run()
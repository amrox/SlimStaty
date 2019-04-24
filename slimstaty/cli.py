# -*- coding: utf-8 -*-

"""Console script for slimstaty."""
import sys
import click
import os
from .slimstaty import StateMachine


def render(state_machine: StateMachine, out_dirpath, **kwargs):
    import jinja2

    from jinja2 import Environment, PackageLoader
    env = Environment(loader=PackageLoader('slimstaty', 'templates'))
    template = env.get_template('java.j2')  # TODO: fix
    outputText = template.render(
        statemachine=state_machine,
        **kwargs)
    print(outputText)


@click.command()
@click.option('--statemachine', help='State Machine Definition (yaml).',
              required=True)
@click.option('--java-package', help='Java package name.')
@click.option('--java-out', help='Java output root.')
def main(statemachine, java_package, java_out, args=None):
    """Slim State Machine Generator"""

    s = StateMachine.from_yaml(statemachine)
    if java_out:
        assert java_package
        render(s, java_out, java_package=java_package)

    return 0


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    sys.exit(main())  # pragma: no cover

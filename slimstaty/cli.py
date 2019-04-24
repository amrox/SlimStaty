# -*- coding: utf-8 -*-

"""Console script for slimstaty."""
import sys
import click
import os
from .slimstaty import StateMachine


def render_java(state_machine, java_out, java_package):
    import jinja2

    from jinja2 import Environment, PackageLoader
    env = Environment(loader=PackageLoader('slimstaty', 'templates'))
    template = env.get_template('java.j2')
    outputText = template.render(
        java_package=java_package,
        statemachine=state_machine)
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

        render_java(s, java_out, java_package)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

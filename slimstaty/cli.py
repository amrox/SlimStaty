# -*- coding: utf-8 -*-

"""Console script for slimstaty."""
import sys
import click
import os
from .slimstaty import StateMachine



def render_java(state_machine, java_out, java_package):
    import jinja2
    p = os.path.join(os.path.dirname(__file__), 'templates', 'java.j2')

    from jinja2 import Environment, PackageLoader
    env = Environment(loader=PackageLoader('slimstaty', 'templates'))
    template = env.get_template('java.j2')
    outputText = template.render(
        java_package=java_package,
        statemachine_name=state_machine.name.title(),
        states=state_machine.states,
        events=state_machine.events,
        transitions=state_machine.transitions)
    print(outputText)
    




@click.command()
@click.option('--statemachine', help='State Machine Definition (yaml).', required=True)
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

# -*- coding: utf-8 -*-

"""Console script for slimstaty."""
import sys
import click
import os
from jinja2 import Environment, PackageLoader, Template
from .slimstaty import StateMachine, render


@click.command()
@click.option('--statemachine', help='State Machine Definition (yaml).',
              required=True)
@click.option('--java-package', help='Java package name.')
@click.option('--java-out', help='Java output root.')
@click.option('--objc-out', help='Objective-C output root.')
@click.option('--objc-prefix', help='Objective-C prefix.', default="")
def main(statemachine,
         java_package, java_out,
         objc_out, objc_prefix, args=None):
    """Slim State Machine Generator"""

    sm = StateMachine.from_yaml(statemachine)
    env = Environment(loader=PackageLoader('slimstaty', 'templates'))

    if java_out:
        assert java_package

        if not os.path.exists(java_out):
            os.makedirs(java_out)

        template = env.get_template('java/java.j2')
        out = render(state_machine=sm, template=template,
                     java_package=java_package)

        filename = f'{sm.name.title()}.java'
        path = os.path.join(java_out, filename)
        with open(path, 'w') as f:
            f.write(out)

    if objc_out:
        if not os.path.exists(objc_out):
            os.makedirs(objc_out)

        statemachine_name = sm.name.title() + "StateMachine"
        statemachine_fname = objc_prefix + statemachine_name

        template = env.get_template('objc/objc.h.j2')
        out = render(state_machine=sm, template=template,
                     statemachine_name=statemachine_name,
                     objc_prefix=objc_prefix)

        filename = f'{statemachine_fname}.h'
        path = os.path.join(java_out, filename)
        with open(path, 'w') as f:
            f.write(out)

        template = env.get_template('objc/objc.m.j2')
        out = render(state_machine=sm, template=template,
                     statemachine_name=statemachine_name,
                     objc_prefix=objc_prefix)

        filename = f'{statemachine_fname}.m'
        path = os.path.join(java_out, filename)
        with open(path, 'w') as f:
            f.write(out)

    return 0


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    sys.exit(main())  # pragma: no cover

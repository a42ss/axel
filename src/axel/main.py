from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from axel.core.exc import AxelError
from axel.controllers.base import Base

# configuration defaults
CONFIG = init_defaults('axel')
CONFIG['axel']['foo'] = 'bar'


class Axel(App):
    """AxelCli primary application."""

    class Meta:
        label = 'axel'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        template_dir = '/axel/templates'
        template_dirs = [
            '~/.axel/templates',
            '~/.config/axel/templates',
            '/usr/lib/axel/templates',
        ]

        # register handlers
        handlers = [
            Base
        ]


class AxelTest(TestApp, Axel):
    """A sub-class of Axel that is better suited for testing."""

    class Meta:
        label = 'axel'


def main():
    with Axel() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except AxelError as e:
            print('AxelError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()

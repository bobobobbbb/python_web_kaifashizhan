from falsk.cli import with_appcontext
import sys

try:
    import IPython
    has_ipython = True
except ImportError:
    has_ipython = False

def plain_shell(user_ns, banner):
    sys.exit(code.interact(banner=banner, local=user_ns))

def ipython_shell(user_ns, banner):
    IPython.embed(banner1=banner, user_ns=user_ns)

@app.cli.command('new_shell', short_help='Runs a shell in app_context')
@click.option('--plain', help='User Plain Shell', is_flag = True)
@with_appcontext
def shell_command(plain):
    from flask.globals import _app_ctx_stack
    app = _app_ctx_stack.top.app
    banner = 'Python %s on %s\nApp: %s%s\nInstance: %s' % (
        sys.version,
        sys.platform,
        app.import_name,
        app.debug and ' [debug]' or '',
        app.instance_path,
    )
    user_ns = app.make_shell_context()
    user_plain_shell = not has_ipython or plain
    if use_plain_shell:
        plain_shell(user_ns, banner)
    else:
        ipython_shell(user_ns, banner)

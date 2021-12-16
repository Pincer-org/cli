import sys
import argparse
import aiohttp
import websockets
import pincer
import pkg_resources
import platform


def show_version():
    entries = []

    entries.append('- Python v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}'.format(sys.version_info))
    version_info = pincer.version_info
    entries.append('- pincer v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}'.format(version_info))
    if version_info.releaselevel != 'final':
        pkg = pkg_resources.get_distribution('pincer')
        if pkg:
            entries.append(f'    - pincer pkg_resources: v{pkg.version}')

    entries.append(f'- aiohttp v{aiohttp.__version__}')
    entries.append(f'- websockets v{websockets.__version__}')
    uname = platform.uname()
    entries.append('- system info: {0.system} {0.release} {0.version}'.format(uname))
    print('\n'.join(entries))

def core(parser, args):
    if args.version:
        show_version()

def parse_args():
    parser = argparse.ArgumentParser(prog='pincercli', description='Pincer CLI Functions') # Doesn't effect you doing python -m pincercli insead of python -m pincer.
    parser.add_argument('-v', '--version', action='store_true', help='Shows the library version')
    parser.set_defaults(func=core)

    # subparser = parser.add_subparsers(dest='subcommand', title='subcommands')
    # new_bot_args(subparser) TODO: Make Basic Bot Template plus more.
    return parser, parser.parse_args()

def main():
    parser, args = parse_args()
    args.func(parser, args)


if __name__ == '__main__':
    main()

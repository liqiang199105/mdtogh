"""\
mdtogh.command
-------------------

Implements the command-line interface for md to github.


Usage:
  mdtogh [options] [<path>]
  mdtogh -h | --help
  mdtogh --version

Where:
  <path> is a file or a directory to render, [default: '.']

Options:
  --cache_path=<path> path to store style file cache
  --css				  when NOT set, css contents are generate into html
  --rlcss			  link css with relative path, use only with --css is set 
  --gfm               Use GitHub-Flavored Markdown, e.g. comments or issues
  --context=<repo>    The repository context, only taken into account with --gfm
  --user=<username>   GitHub username for API authentication
  --pass=<password>   GitHub password for API authentication
  --toc               Generate table of contents
  --offline           Use offline renderer
  --refresh           clear cached styles & refetch them
"""

import sys
from docopt import docopt
import json 
from .transform import transform
from . import __version__

usage = '\n\n\n'.join(__doc__.split('\n\n\n')[1:])

def main(argv=None):
    """Entry point of this application"""
    if argv is None:
        argv = sys.argv[1:]
    version = 'mdtogh ' + __version__

    args = docopt(usage, argv=argv, version=version)

    json.dump(args, sys.stdout)

    try:
       transform(args['<path>'], args['--cache_path'], args['--css'], args['--rlcss'], args['--gfm'], args['--user'],args['--pass'], args['--toc'], args['--offline'], args['--refresh'])
       return 0
    except ValueError as e:
        print "Error: ", e
        return 1

if __name__ == '__main__':
	main()

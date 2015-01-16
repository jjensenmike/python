"""
This is an example script that uses argparse and a main function to accept
  command line parameters and process them when the script is run as the main
  script.

To Run:
    From the command line, enter: python argparse_ex.py -n <screenname>

"""

from argparse import ArgumentParser


def main():
    """main function run when called from the conditional below. Creates the
    parser object, parses the responses, and prints out the screenname if one
    is provided from the command line
    """

    usage = 'Collect screenname info'
    parser = ArgumentParser(usage=usage)
    parser.add_argument('-n', action='store', dest='screenname', default=None,
                        help='screen name to pull information about')
    args = parser.parse_args()

    if args.screenname:
        print 'Screen name to check: {}'.format(args.screenname)
    else:
        print 'No screen name info!!!'

if __name__ == '__main__':
    main()

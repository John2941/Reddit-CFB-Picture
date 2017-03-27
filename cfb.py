#!/usr/bin/python
"""
@Project Name - cfb
@author - Johnathan
@date - 10/2/2016
@time - 1:11 PM

"""

import praw
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--time', dest='time', action='store', default='week',
                    help='(WEEK | MONTH | YEAR) Time to search')
parser.add_argument('-s', '--search', dest='search', action='store', default=['Tennessee', 'Georgia'], nargs='+',
                    help='Teams to search. Space separated')
parser.add_argument('-a', '--all', dest='searchAllTeams', action='store_true', default=False,
                    help='Flag. Search all teams')
args = parser.parse_args()

cfb_threads = praw.Reddit(user_agent='CFB App')

if args.searchAllTeams:
    args.search = ''
else:
    args.search = ' OR '.join(args.search)
    args.search = '(' + args.search + ')'

if args.time.lower() not in ['week', 'month', 'year']:
    parser.error('-t (WEEK | MONTH | YEAR)')

print 'Searching for: {0}'.format(args.search if args.search else 'All teams')

for thread in cfb_threads.search('[Post Game Thread] AND ({0})'.format(args.search), subreddit='CFB', period=args.time):
    if '[Post Game Thread]' in thread.title:
        print thread.title
        try:
            print thread.preview['images'][0]['source']['url']
        except AttributeError:
            print "No URL"

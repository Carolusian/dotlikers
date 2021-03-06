#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File: fblikers/main.py
# Author: Carolusian <https://github.com/carolusian>
# Date: 29.07.2017
# Last Modified Date: 30.07.2017
#
# Copyright 2017 Carolusian

import argparse
from .users import load_users, FacebookUser, InstagramUser
from .actions import login, sleep, USER_ACTIONS


def main(args):
    """Entrypoint of dotlikers"""
    all_users = load_users(args['credentials'])
    action_types = [ action for action in args['actions'].split(',') if action]
    target_url = args['target_url']

    # select correspond users for the target url
    if is_facebook(target_url):
        users = [u for u in all_users if isinstance(u, FacebookUser)]

    if is_instagram(target_url):
        users = [u for u in all_users if isinstance(u, InstagramUser)]

    for user in users:
        sleep()
        browser = login(user)
        sleep()
        for action_type in action_types:
            USER_ACTIONS[action_type](user, target_url, browser)
        # browser.quit()


def is_facebook(url):
    return 'facebook.com' in url


def is_instagram(url):
    return 'instagram.com' in url


def get_parser():
    """Define an argument parser"""
    parser = argparse.ArgumentParser(
        description='reduce your effort to act as likers'
    )
    parser.add_argument('credentials',
                        help='- credential file of usernames and passwords')
    parser.add_argument('actions',
                        help='- tell what kind of action the users will take')
    parser.add_argument('target_url',
                        help='- the url of the target of the action')
    return parser


def command_line_runner(args=[]):
    parser = get_parser()
    if len(args):
        args = vars(parser.parse_args(args))
    else:
        args = vars(parser.parse_args())
    main(args)


if __name__ == '__main__':
    # parse command line arguments and run the main function
    command_line_runner()

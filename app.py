#!/usr/bin/env python3
import connexion
import datetime
import logging
import jt_ams

from connexion import NoContent


def get_accounts(limit, offset):
    return []


def get_account(account_name):
    account = jt_ams.get_account(account_name)
    return account or ('Not found', 404)


def create_account(account):
    account_name = account.get('_name')
    account_type = account.get('account_type') or 'org'

    exists = jt_ams.get_account(account_name)
    if exists:
        return NoContent, 409
    else:
        return jt_ams.create_account(account_name, account_type)


def update_account(account_id):
    pass


def delete_account(account_id):
    pass


def get_member(account_name, member_id):
    pass


def add_member(account_name, member_id):
    pass


def delete_member(account_name, member_id):
    pass


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger.yaml', base_path='/api/jt-ams/v0.1')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=1206, server='gevent')

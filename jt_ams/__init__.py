__version__ = '0.2.0a6'

from . import ams


def get_accounts(limit, offset):
    return []


def get_account(account_name):
    return ams.get_account(account_name) or ('Not found', 404)


def get_account_by_id(account_id):
    return ams.get_account_by_id(account_id) or ('Not found', 404)


def create_account(account):
    account_name = account.get('name')
    account_type = account.get('account_type') or 'org'

    exists = ams.get_account(account_name)
    if exists:
        return "Account name already exists", 409
    else:
        return ams.create_account(account_name, account_type)


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

import etcd3
import uuid

# settings, need to move out to config

AMS_ETCD_ROOT = '/jthub:ams'
ACCOUNT_PREFIX = 'account'
ACCOUNT_MK = 'name'  # main key field for account
ACCOUNT_PK = 'id'

etcd_client = etcd3.client()


def get_accounts(account_name):
    pass


def get_account_by_id(account_id):
    account = {
        'id': account_id
    }

    key_prefix = '/'.join([AMS_ETCD_ROOT, ACCOUNT_PREFIX, '%s:%s/' % (ACCOUNT_PK, account_id)])
    r = etcd_client.get_prefix(key_prefix=key_prefix, sort_target='KEY')

    for value, meta in r:
        k = meta.key.decode('utf-8').replace(key_prefix, '', 1)
        try:
            v = value.decode("utf-8")
        except:
            v = None  # assume binary value, deal with it later

        if ':' in k:
            k, v = k.split(':', 1)

        if k.startswith('is_'):
            v = True if v and v != '0' else False

        if '@' not in k:
            account[k] = v
        else:
            sub_key, sub_type = k.split('@', 1)
            if sub_type not in account:
                account[sub_type] = []
            account[sub_type].append({sub_key: v})

    if account.get('name'): # account must have 'name'
        return account


def get_account(account_name):
    # get primary ID from account name
    key = '/'.join([AMS_ETCD_ROOT, ACCOUNT_PREFIX, '%s:%s' % (ACCOUNT_MK, account_name)])
    r = etcd_client.get(key)

    try:
        account_id = r[0].decode("utf-8")
    except:
        return

    return get_account_by_id(account_id)


def create_account(account_name, account_type):
    account_id = str(uuid.uuid4())  # generate random UUID as primary ID

    key = '/'.join([AMS_ETCD_ROOT, ACCOUNT_PREFIX, '%s:%s' % (ACCOUNT_MK, account_name)])
    r = etcd_client.put(key, account_id)

    key_prefix = '/'.join([AMS_ETCD_ROOT, ACCOUNT_PREFIX, '%s:%s' % (ACCOUNT_PK, account_id)])
    r = etcd_client.put('%s/%s:%s' % (key_prefix, ACCOUNT_MK, account_name), '')

    if account_type == 'org':
        r = etcd_client.put('%s/is_org:1' % key_prefix, '')
    else:
        r = etcd_client.put('%s/is_org:0' % key_prefix, '')

    return get_account(account_name)


def update_account():
    pass


def delete_account():
    pass


def add_member():
    pass


def get_member():
    pass


def delete_member():
    pass

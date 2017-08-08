import etcd3
import uuid

# settings, need to move out to config

AMS_ETCD_ROOT = '/jthub:ams'
ACCOUNT_PREFIX = 'account@accounts'

etcd_client = etcd3.client()


def get_accounts(account_name):
    pass


def get_account(account_name):
    key = '/'.join([AMS_ETCD_ROOT, ACCOUNT_PREFIX, '%s:%s' % ('_name', account_name)])
    r = etcd_client.get(key)

    try:
        _id = r[0].decode("utf-8")
    except:
        return

    account = {
        '_id': _id
    }

    key_prefix = '/'.join([AMS_ETCD_ROOT, ACCOUNT_PREFIX, 'data', '%s:%s/' % ('_id', _id)])
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
            if not sub_type in account: account[sub_type] = []
            account[sub_type].append({sub_key: v})

    return account


def create_account(account_name, account_type):
    _id = str(uuid.uuid4())

    key = '/'.join([AMS_ETCD_ROOT, ACCOUNT_PREFIX, '%s:%s' % ('_name', account_name)])
    r = etcd_client.put(key, _id)

    key_prefix = '/'.join([AMS_ETCD_ROOT, ACCOUNT_PREFIX, 'data', '%s:%s' % ('_id', _id)])
    r = etcd_client.put('%s/_name' % key_prefix, account_name)

    if account_type == 'org':
        r = etcd_client.put('%s/is_org' % key_prefix, '1')
    else:
        r = etcd_client.put('%s/is_org' % key_prefix, '')

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

import ldap3

from ldap_test import LdapServer

server = LdapServer({
    'port': 3333,
    'bind_dn': 'cn=admin,dc=luochunhui,dc=com',
    'password': 'pass1',
    'base': {'objectclass': ['domain'],
             'dn': 'dc=luochunhui,dc=com',
             'attributes': {'dc': 'luochunhui'}},
    'entries': [
        {'objectclass': 'domain',
         'dn': 'dc=users,dc=luochunhui,dc=com',
         'attributes': {'dc': 'users'}},
        {'objectclass': 'organization',
         'dn': 'o=foocompany,dc=users,dc=luochunhui,dc=com',
         'attributes': {'o': 'foocompany'}},
    ]
})

try:
    server.start()

    dn = "cn=admin,dc=luochunhui,dc=com"
    pw = "pass1"

    srv = ldap3.Server('localhost', port=3333)
    conn = ldap3.Connection(srv, user=dn, password=pw, auto_bind=True)

    base_dn = 'dc=luochunhui,dc=com'
    search_filter = '(objectclass=organization)'
    attrs = ['o']

    conn.search(base_dn, search_filter, attributes=attrs)

    print conn.response
    # [{
    #    'dn': 'o=foocompany,dc=users,dc=luochunhui,dc=com',
    #    'raw_attributes': {'o': [b'foocompany']},
    #    'attributes': {'o': ['foocompany']},
    #    'type': 'searchResEntry'
    # }]
finally:
    server.stop()
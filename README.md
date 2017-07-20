Ansible Role: postfix-null-client
=================================

[![Build Status](https://travis-ci.org/giovtorres/ansible-role-postfix-null-client.svg?branch=master)](https://travis-ci.org/giovtorres/ansible-role-postfix-null-client)
[![Ansible Role](https://img.shields.io/ansible/role/19344.svg)](https://galaxy.ansible.com/giovtorres/postfix-null-client/)

This role installs postfix on a [null
client](http://www.postfix.org/STANDARD_CONFIGURATION_README.html#null_client).
Supported on EL6 and EL7.

Requirements
------------

None.

Role Variables
--------------

> Note, the only variable you should change is the `relayhost`.  The other
> variables are part of the null client configuration.

Set the `myhostname` to the FQDN of the machine:

    postfix_myhostname: "{{ ansible_fqdn }}"

`mydomain` is used as a default for the `relayhost` even though it is not
explicitly part of the null client configuration:

    postfix_mydomain: "{{ ansible_domain }}"

Locally sent mail will appear to come from this domain.  If there are many
machines on the network configured as null clients, setting this to
`$myhostname` could help identify the source of the mail.  This could also be set to
`$mydomain` so that mail doesn't inadvertently get sent to this null client
machine:

    postfix_myorigin: "$myhostname"

Forward all messages to this mail server.  Square brackets around the hostname
will prevent MX record lookups:

    postfix_relayhost: "$mydomain"

Listen only on the loopback interface and do not accept mail from the network:

    postfix_inet_interfaces: "loopback-only"

Disable local delivery altogether:

    postfix_local_transport: "error: local delivery disabled"

Only accept mail from localhost:

    postfix_mynetworks: "127.0.0.0/8 [::1]/128"

List of trusted networks for relay access.  `host` tells Postfix to only trust
the local machine.  This has the same effect as the `postfix_mynetworks`
setting above, but better to be explicit:

    postfix_mynetworks_style: host

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      vars:
        postfix_relayhost: "relay01.example.com"
      roles:
         - giovtorres.postfix-null-client

License
-------

BSD

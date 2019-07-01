import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postfix_package(host):
    assert host.package("postfix").is_installed


def test_postfix_service(host):
    s = host.service("postfix")
    assert s.is_running
    assert s.is_enabled


def test_postfix_socket(host):
    assert host.socket("tcp://127.0.0.1:25").is_listening


def test_postfix_null_client_config(host):
    assert "= null-client.example.com" in host.check_output(
        "postconf myhostname"
    )
    assert "= example.com" in host.check_output("postconf mydomain")
    assert "= $myhostname" in host.check_output("postconf myorigin")
    assert "= $mydomain" in host.check_output("postconf relayhost")
    assert "= loopback-only" in host.check_output("postconf inet_interfaces")
    assert "= error: local delivery disabled" in host.check_output(
        "postconf local_transport"
    )
    assert "= 127.0.0.0/8 [::1]/128" in host.check_output(
        "postconf mynetworks"
    )
    assert "= host" in host.check_output("postconf mynetworks_style")
    assert "mydestination =" in host.check_output("postconf mydestination")

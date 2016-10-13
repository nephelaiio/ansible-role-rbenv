from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = \
    AnsibleRunner('.molecule/ansible_inventory').get_hosts('install')


def test_command(Command):
    assert Command('/bin/bash -l -c "rbenv --version"').rc == 0

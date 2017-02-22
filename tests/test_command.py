from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = \
    AnsibleRunner('.molecule/ansible_inventory').get_hosts('install')


def test_command(Command):
    cmd = '/bin/bash -l -c "rbenv --version"'
    assert Command(cmd).rc == 0

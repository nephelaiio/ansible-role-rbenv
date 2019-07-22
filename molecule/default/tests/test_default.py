import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rbenv_bin(host.command):
    cmd = '/bin/bash -l -c "rbenv --version"'
    assert host.command(cmd).rc == 0

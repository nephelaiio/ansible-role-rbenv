import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

versions = ['2.4.1']


def test_rbenv_bin(Command):
    cmd = '/bin/bash -l -c "rbenv --version"'
    assert Command(cmd).rc == 0


def test_rbenv_version(Command):
    for version in versions:
        cmd_tpl = "/bin/bash -l -c \"rbenv versions --bare | grep {0}\""
        cmd = cmd_tpl.format(version)
        assert Command(cmd).rc == 0


def test_rbenv_local(Command):
    for version in versions:
        cmd_tpl = "/bin/bash -l -c \"rbenv local | grep {0}\""
        cmd = cmd_tpl.format(version)
        assert Command(cmd).rc == 0

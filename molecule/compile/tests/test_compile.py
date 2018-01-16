import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ruby_version = '2.4.1'


def test_rbenv_version(host):
    cmd = '~/.rbenv/bin/rbenv versions --bare'
    assert host.check_output(cmd) == ruby_version


def test_gem(host):
    cmd = '~/.rbenv/versions/2.4.1/bin/gem list | grep sensu'
    assert host.run(cmd).rc == 0


def test_ruby_home(host):
    ruby = '/opt/rbenv/.rbenv/versions/2.4.1'
    assert host.file('/opt/ruby').exists
    assert host.file('/opt/ruby').is_symlink
    assert host.file('/opt/ruby/').linked_to == ruby

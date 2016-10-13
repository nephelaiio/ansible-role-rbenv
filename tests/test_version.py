from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = \
    AnsibleRunner('.molecule/ansible_inventory').get_hosts('compile')


def test_version(Command):
    versions = ['2.3.1', '2.2.5']
    for version in versions:
        cmd_tpl = "/bin/bash -l -c \"rbenv versions --bare | grep {0}\""
        cmd = cmd_tpl.format(version)
        assert Command(cmd).rc == 0

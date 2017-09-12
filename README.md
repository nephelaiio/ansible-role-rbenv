nephelaiio.rbenv
=========

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-rbenv.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-rbenv)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-systemd--service-blue.svg)](https://galaxy.ansible.com/nephelaiio/rbenv/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/rbenv) to install and configure rbenv

Requirements
------------

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](/requirements.txt)

Role Variables
--------------

Please refer to the [defaults file](/defaults/main.yml) for an up-to-date list of input parameters.

Dependencies
------------

Please refer to the [dependency file](/meta/main.yml) for an up-to-date lists of required roles

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: rbenv rbenv_packages: rbenv }


Testing
-------

Role is tested against the following distributions (docker images):
  * Ubuntu Xenial
  * CentOS 7
  * Debian Jessie
  * Arch Linux

You can test the role from sources using the command line using molecule directly
```
molecule test
```

License
-------

This project is licensed under the terms of the [MIT License](/LICENSE)

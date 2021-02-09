.. _a10_admin_ssh_pubkey_module:


a10_admin_ssh_pubkey -- Configures A10 admin.ssh-pubkey
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Config openssh authorized public keys management






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  admin_user (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  list (False, any, None)
    List all authorized public keys


  file_url (False, any, None)
    File URL


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  nimport (False, any, None)
    Import an authorized public key


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  delete (False, any, None)
    Delete an authorized public key (SSH key index)









Examples
--------

.. code-block:: yaml+jinja

    





Status
------




- This module is not guaranteed to have a backwards compatible interface. *[preview]*


- This module is maintained by community.



Authors
~~~~~~~

- A10 Networks 2018


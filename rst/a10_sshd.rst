.. _a10_sshd_module:


a10_sshd -- Configures A10 sshd
===============================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SSHD service operation






Parameters
----------

  load (False, any, None)
    Load SSH key


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  regenerate (False, any, None)
    Wipe and generate SSH key


  ansible_password (True, any, None)
    Password for AXAPI authentication


  file_url (False, any, None)
    File URL


  generate (False, any, None)
    Generate SSH key


  state (True, any, None)
    State of the object to be created.


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ansible_host (True, any, None)
    Host for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  wipe (False, any, None)
    Wipe SSH key


  restart (False, any, None)
    Restart SSH service


  size (False, any, None)
    '2048'= Key size 2048bit; '4096'= Key size 4096bit;









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


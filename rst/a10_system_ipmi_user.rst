.. _a10_system_ipmi_user_module:


a10_system_ipmi_user -- Configures A10 system.ipmi.user
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Add, Change or Disable IPMI users






Parameters
----------

  administrator (False, any, None)
    Full control


  ansible_username (True, any, None)
    Username for AXAPI authentication


  newname (False, any, None)
    New IPMI User Name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  setpass (False, any, None)
    Change Password (IPMI User Name)


  user (False, any, None)
    Only 'benign' commands are allowed


  operator (False, any, None)
    Most BMC commands are allowed


  password (False, any, None)
    Password


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  setname (False, any, None)
    Change User Name (Current IPMI User Name)


  add (False, any, None)
    Add a new IPMI user (IPMI User Name)


  callback (False, any, None)
    Lowest privilege level


  newpass (False, any, None)
    New Password


  disable (False, any, None)
    Disable an existing IPMI user (IPMI User Name)


  privilege (False, any, None)
    Change an existing IPMI user privilege (IPMI User Name)


  ansible_password (True, any, None)
    Password for AXAPI authentication









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


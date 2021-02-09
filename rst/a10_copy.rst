.. _a10_copy_module:


a10_copy -- Configures A10 copy
===============================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Copy configuration to/from remote server






Parameters
----------

  profile (False, any, None)
    From Startup-config Profile


  ansible_username (True, any, None)
    Username for AXAPI authentication


  dest_use_mgmt_port (False, any, None)
    Use management port as destination port


  running_config (False, any, None)
    From Running Config


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  to_running_config (False, any, None)
    To Running Config


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  dest_remote_file (False, any, None)
    Remote file path


  state (True, any, None)
    State of the object to be created.


  ansible_host (True, any, None)
    Host for AXAPI authentication


  startup_config (False, any, None)
    From Startup Config


  to_startup_config (False, any, None)
    To Startup Config


  dest_profile (False, any, None)
    Local Configuration Profile Name


  remote_file (False, any, None)
    Remote file path


  to_profile (False, any, None)
    To Local Configuration Profile









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


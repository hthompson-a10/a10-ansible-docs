.. _a10_system_timeout_value_module:


a10_system_timeout_value -- Configures A10 system.timeout-value
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

set the timeout to stop transferring a file






Parameters
----------

  ftp (False, any, None)
    set timeout to stop ftp transfer in seconds, 0 is no limit


  ansible_port (True, any, None)
    Port for AXAPI authentication


  http (False, any, None)
    set timeout to stop http transfer in seconds, 0 is no limit


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  sftp (False, any, None)
    set timeout to stop sftp transfer in seconds, 0 is no limit


  state (True, any, None)
    State of the object to be created.


  https (False, any, None)
    set timeout to stop https transfer in seconds, 0 is no limit


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ansible_host (True, any, None)
    Host for AXAPI authentication


  tftp (False, any, None)
    set timeout to stop tftp transfer in seconds, 0 is no limit


  a10_partition (False, any, None)
    Destination/target partition for object/command


  scp (False, any, None)
    set timeout to stop scp transfer in seconds, 0 is no limit









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


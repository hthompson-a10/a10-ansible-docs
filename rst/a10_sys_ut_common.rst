.. _a10_sys_ut_common_module:


a10_sys_ut_common -- Configures A10 sys.ut.common
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Common






Parameters
----------

  proceed_on_error (False, any, None)
    Run test even in case of event failure


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  delay (False, any, None)
    wait time in seconds after each run


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication









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


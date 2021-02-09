.. _a10_sys_ut_stop_test_module:


a10_sys_ut_stop_test -- Configures A10 sys.ut.stop-test
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Clear all dynamic test parameters and stop the test






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  state (True, any, None)
    State of the object to be created.


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


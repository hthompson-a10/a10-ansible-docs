.. _a10_sys_ut_run_test_module:


a10_sys_ut_run_test -- Configures A10 sys.ut.run-test
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Run currently setup test






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  mode (False, any, None)
    'basic'= Run Basic mode; 'fault-injection'= Run FI mode. This will also run Basic mode to gather data; 'cpu-rr'= Run CPU RR mode; 'frag'= Run IP frag mode;


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


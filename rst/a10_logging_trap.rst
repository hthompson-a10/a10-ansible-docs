.. _a10_logging_trap_module:


a10_logging_trap -- Configures A10 logging.trap
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set logging level which sent to snmp trap host






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  trap_levelname (False, any, None)
    'disable'= Do not send trap to snmp host; 'emergency'= System unusable log messages      (severity=0); 'alert'= Action must be taken immediately (severity=1); 'critical'= Critical conditions               (severity=2);


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object









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


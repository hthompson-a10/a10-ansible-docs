.. _a10_debug_logging_module:


a10_debug_logging -- Configures A10 debug.logging
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Logging module parameters






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  all (False, any, None)
    Logging all debug switch


  state (True, any, None)
    State of the object to be created.


  command (False, any, None)
    Logging debug command switch


  error (False, any, None)
    Logging debug error switch


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


.. _a10_logging_lsn_log_suppression_module:


a10_logging_lsn_log_suppression -- Configures A10 logging.lsn.log-suppression
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set LSN system log generation parameters






Parameters
----------

  count (False, any, None)
    Configure log suppression count (default= 100)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  time (False, any, None)
    Log generation timeout(default= 30 seconds)


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


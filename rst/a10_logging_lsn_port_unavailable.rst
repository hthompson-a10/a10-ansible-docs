.. _a10_logging_lsn_port_unavailable_module:


a10_logging_lsn_port_unavailable -- Configures A10 logging.lsn.port-unavailable
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set LSN system log policy when port unavailable occur






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


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ip_based (False, any, None)
    Log LSN port unavailable based on NAT IP (Default= disabled)


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


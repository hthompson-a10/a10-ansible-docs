.. _a10_sflow_collector_ip_module:


a10_sflow_collector_ip -- Configures A10 sflow.collector.ip
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure sFlow IPv4 collector






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  addr (True, any, None)
    Configure sFlow collector IP address


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (True, any, None)
    Port number (default is 6343)


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


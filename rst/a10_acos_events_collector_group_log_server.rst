.. _a10_acos_events_collector_group_log_server_module:


a10_acos_events_collector_group_log_server -- Configures A10 acos-events.collector.group.log-server
===================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure log server DNS Name/ip-address and optional port






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Member name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  collector_group_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (True, any, None)
    Port number


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


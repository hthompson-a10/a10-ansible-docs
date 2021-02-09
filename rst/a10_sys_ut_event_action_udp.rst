.. _a10_sys_ut_event_action_udp_module:


a10_sys_ut_event_action_udp -- Configures A10 sys.ut.event.action.udp
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

UDP header






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  dest_port_value (False, any, None)
    Dest port value


  nat_pool (False, any, None)
    Nat pool port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  dest_port (False, any, None)
    Dest port


  ansible_port (True, any, None)
    Port for AXAPI authentication


  src_port (False, any, None)
    Source port value


  uuid (False, any, None)
    uuid of the object


  event_number (optional, any, None)
    Key to identify parent object


  length (False, any, None)
    Total packet length starting at UDP header


  state (True, any, None)
    State of the object to be created.


  checksum (False, any, None)
    'valid'= valid; 'invalid'= invalid;


  action_direction (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication









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


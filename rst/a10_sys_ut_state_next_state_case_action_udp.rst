.. _a10_sys_ut_state_next_state_case_action_udp_module:


a10_sys_ut_state_next_state_case_action_udp -- Configures A10 sys.ut.state.next.state.case.action.udp
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

UDP header






Parameters
----------

  state_name (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  dest_port_value (False, any, None)
    Dest port value


  nat_pool (False, any, None)
    Nat pool port


  case_number (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (optional, any, None)
    Key to identify parent object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  src_port (False, any, None)
    Source port value


  uuid (False, any, None)
    uuid of the object


  checksum (False, any, None)
    'valid'= valid; 'invalid'= invalid;


  length (False, any, None)
    Total packet length starting at UDP header


  state (True, any, None)
    State of the object to be created.


  action_direction (optional, any, None)
    Key to identify parent object


  dest_port (False, any, None)
    Dest port


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


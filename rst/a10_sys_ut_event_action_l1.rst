.. _a10_sys_ut_event_action_l1_module:


a10_sys_ut_event_action_l1 -- Configures A10 sys.ut.event.action.l1
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

L1 packet paramters






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  auto (False, any, None)
    Auto calculate pkt len


  state (True, any, None)
    State of the object to be created.


  value (False, any, None)
    Total packet length starting at L2 header


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  length (False, any, None)
    packet length


  eth_list (False, any, None)
    Field eth_list


    ethernet_start (optional, any, None)
      Ethernet port (Interface number)


    ethernet_end (optional, any, None)
      Ethernet port



  event_number (optional, any, None)
    Key to identify parent object


  action_direction (optional, any, None)
    Key to identify parent object


  trunk_list (False, any, None)
    Field trunk_list


    trunk_start (optional, any, None)
      Trunk groups


    trunk_end (optional, any, None)
      Trunk Group



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


.. _a10_sys_ut_state_next_state_case_module:


a10_sys_ut_state_next_state_case -- Configures A10 sys-ut.state.next.state.case
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Case number






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  repeat (False, any, None)
    number of times case should be repeated before state transition


  name (optional, any, None)
    Key to identify parent object


  action_list (False, any, None)
    Field action_list


    direction (optional, any, None)
      'send'= Test event; 'expect'= Expected result; 'wait'= Introduce a delay;


    uuid (optional, any, None)
      uuid of the object


    drop (optional, any, None)
      Packet drop. Only allowed for output spec


    udp (optional, any, None)
      Field udp


    tcp (optional, any, None)
      Field tcp


    delay (optional, any, None)
      Delay in seconds


    l2 (optional, any, None)
      Field l2


    l3 (optional, any, None)
      Field l3


    template (optional, any, None)
      Packet template


    l1 (optional, any, None)
      Field l1



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  state_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  case_number (True, any, None)
    Field case_number


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


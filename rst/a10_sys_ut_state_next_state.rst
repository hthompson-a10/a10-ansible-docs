.. _a10_sys_ut_state_next_state_module:


a10_sys_ut_state_next_state -- Configures A10 sys-ut.state.next-state
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Next State machine node






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  state_name (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  case_list (False, any, None)
    Field case_list


    repeat (optional, any, None)
      number of times case should be repeated before state transition


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object


    action_list (optional, any, None)
      Field action_list


    case_number (optional, any, None)
      Field case_number



  name (True, any, None)
    Node name


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


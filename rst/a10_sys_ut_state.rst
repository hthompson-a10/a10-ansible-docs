.. _a10_sys_ut_state_module:


a10_sys_ut_state -- Configures A10 sys-ut.state
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

State machine node






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Node name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  next_state_list (False, any, None)
    Field next_state_list


    user_tag (optional, any, None)
      Customized tag


    name (optional, any, None)
      Node name


    case_list (optional, any, None)
      Field case_list


    uuid (optional, any, None)
      uuid of the object



  ansible_password (True, any, None)
    Password for AXAPI authentication


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


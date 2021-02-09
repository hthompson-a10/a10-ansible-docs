.. _a10_sys_ut_event_module:


a10_sys_ut_event -- Configures A10 sys-ut.event
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify event parameters






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  action_list (False, any, None)
    Field action_list


    direction (optional, any, None)
      'send'= Test event; 'expect'= Expected result; 'wait'= Introduce a delay;


    uuid (optional, any, None)
      uuid of the object


    ignore_validation (optional, any, None)
      Field ignore_validation


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


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  event_number (True, any, None)
    Event number


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


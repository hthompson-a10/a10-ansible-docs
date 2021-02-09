.. _a10_sys_ut_module:


a10_sys_ut -- Configures A10 sys-ut
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

System unit test






Parameters
----------

  template_list (False, any, None)
    Field template_list


    udp (optional, any, None)
      Field udp


    name (optional, any, None)
      template name


    ignore_validation (optional, any, None)
      Field ignore_validation


    tcp (optional, any, None)
      Field tcp


    l2 (optional, any, None)
      Field l2


    l3 (optional, any, None)
      Field l3


    l1 (optional, any, None)
      Field l1


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object



  ansible_port (True, any, None)
    Port for AXAPI authentication


  state_list (False, any, None)
    Field state_list


    uuid (optional, any, None)
      uuid of the object


    user_tag (optional, any, None)
      Customized tag


    name (optional, any, None)
      Node name


    next_state_list (optional, any, None)
      Field next_state_list



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  common (False, any, None)
    Field common


    delay (optional, any, None)
      wait time in seconds after each run


    proceed_on_error (optional, any, None)
      Run test even in case of event failure


    uuid (optional, any, None)
      uuid of the object



  test_name (False, any, None)
    Name for this test case


  action (False, any, None)
    'enable'= Set device to SUT mode; 'disable'= Set device to normal mode;


  run_test (False, any, None)
    Field run_test


    mode (optional, any, None)
      'basic'= Run Basic mode; 'fault-injection'= Run FI mode. This will also run Basic mode to gather data; 'cpu-rr'= Run CPU RR mode; 'frag'= Run IP frag mode;



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  event_list (False, any, None)
    Field event_list


    event_number (optional, any, None)
      Event number


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object


    action_list (optional, any, None)
      Field action_list










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


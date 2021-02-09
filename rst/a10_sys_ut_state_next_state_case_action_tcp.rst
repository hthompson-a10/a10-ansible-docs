.. _a10_sys_ut_state_next_state_case_action_tcp_module:


a10_sys_ut_state_next_state_case_action_tcp -- Configures A10 sys.ut.state.next.state.case.action.tcp
=====================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

TCP header






Parameters
----------

  state_name (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  dest_port_value (False, any, None)
    Dest port value


  urgent (False, any, None)
    'valid'= valid; 'invalid'= invalid;


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


  dest_port (False, any, None)
    Dest port


  ansible_port (True, any, None)
    Port for AXAPI authentication


  src_port (False, any, None)
    Source port value


  uuid (False, any, None)
    uuid of the object


  seq_number (False, any, None)
    'valid'= valid; 'invalid'= invalid;


  checksum (False, any, None)
    'valid'= valid; 'invalid'= invalid;


  state (True, any, None)
    State of the object to be created.


  name (optional, any, None)
    Key to identify parent object


  window (False, any, None)
    'valid'= valid; 'invalid'= invalid;


  ack_seq_number (False, any, None)
    'valid'= valid; 'invalid'= invalid;


  flags (False, any, None)
    Field flags


    psh (optional, any, None)
      Psh


    urg (optional, any, None)
      Urg


    uuid (optional, any, None)
      uuid of the object


    ack (optional, any, None)
      Ack


    cwr (optional, any, None)
      Cwr


    ece (optional, any, None)
      Ece


    syn (optional, any, None)
      Syn


    rst (optional, any, None)
      Rst


    fin (optional, any, None)
      Fin



  action_direction (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  options (False, any, None)
    Field options


    sack_type (optional, any, None)
      'permitted'= permitted; 'block'= block;


    uuid (optional, any, None)
      uuid of the object


    nop (optional, any, None)
      No Op


    time_stamp_enable (optional, any, None)
      adds Time Stamp to options


    mss (optional, any, None)
      TCP MSS


    wscale (optional, any, None)
      Field wscale










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


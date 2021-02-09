.. _a10_slb_mlb_module:


a10_slb_mlb -- Configures A10 slb.mlb
=====================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure mlb






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'client_msg_sent'= Client message sent; 'server_msg_received'= Server message received; 'server_conn_created'= Server connection created; 'server_conn_rst'= Server connection reset; 'server_conn_failed'= Server connection failed; 'server_conn_closed'= Server connection closed; 'client_conn_created'= Client connection created; 'client_conn_closed'= Client connection closed; 'client_conn_not_found'= Client connection not found; 'msg_dropped'= Message dropped; 'mlb_dcmsg_sent'= Dcmsg sent; 'mlb_dcmsg_received'= Dcmsg received; 'mlb_dcmsg_error'= Dcmsg error; 'mlb_dcmsg_alloc'= Dcmsg alloc; 'mlb_dcmsg_free'= Dcmsg free;



  oper (False, any, None)
    Field oper


    l4_cpu_list (optional, any, None)
      Field l4_cpu_list


    cpu_count (optional, any, None)
      Field cpu_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    server_conn_closed (optional, any, None)
      Server connection closed


    msg_dropped (optional, any, None)
      Message dropped


    server_conn_created (optional, any, None)
      Server connection created


    mlb_dcmsg_alloc (optional, any, None)
      Dcmsg alloc


    client_conn_not_found (optional, any, None)
      Client connection not found


    server_conn_rst (optional, any, None)
      Server connection reset


    mlb_dcmsg_received (optional, any, None)
      Dcmsg received


    server_conn_failed (optional, any, None)
      Server connection failed


    client_msg_sent (optional, any, None)
      Client message sent


    mlb_dcmsg_error (optional, any, None)
      Dcmsg error


    client_conn_created (optional, any, None)
      Client connection created


    mlb_dcmsg_free (optional, any, None)
      Dcmsg free


    server_msg_received (optional, any, None)
      Server message received


    client_conn_closed (optional, any, None)
      Client connection closed


    mlb_dcmsg_sent (optional, any, None)
      Dcmsg sent



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


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


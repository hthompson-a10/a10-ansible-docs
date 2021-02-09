.. _a10_slb_fix_module:


a10_slb_fix -- Configures A10 slb.fix
=====================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure FIX Proxy






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'curr_proxy'= Current proxy conns; 'total_proxy'= Total proxy conns; 'svrsel_fail'= Server selection failure; 'noroute'= No route failure; 'snat_fail'= Source NAT failure; 'client_err'= Client fail; 'server_err'= Server fail; 'insert_clientip'= Insert client IP; 'default_switching'= Default switching; 'sender_switching'= Sender ID switching; 'target_switching'= Target ID switching;



  oper (False, any, None)
    Field oper


    cpu_count (optional, any, None)
      Field cpu_count


    fix_cpu_list (optional, any, None)
      Field fix_cpu_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    svrsel_fail (optional, any, None)
      Server selection failure


    default_switching (optional, any, None)
      Default switching


    total_proxy (optional, any, None)
      Total proxy conns


    curr_proxy (optional, any, None)
      Current proxy conns


    sender_switching (optional, any, None)
      Sender ID switching


    noroute (optional, any, None)
      No route failure


    client_err (optional, any, None)
      Client fail


    target_switching (optional, any, None)
      Target ID switching


    server_err (optional, any, None)
      Server fail


    snat_fail (optional, any, None)
      Source NAT failure


    insert_clientip (optional, any, None)
      Insert client IP



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


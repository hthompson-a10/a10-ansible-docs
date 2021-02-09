.. _a10_slb_connection_reuse_module:


a10_slb_connection_reuse -- Configures A10 slb.connection-reuse
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Connection Reuse






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'current_open'= Open persist; 'current_active'= Active persist; 'nbind'= Total bind; 'nunbind'= Total unbind; 'nestab'= Total established; 'ntermi'= Total terminated; 'ntermi_err'= Total terminated by err; 'delay_unbind'= Delayed unbind; 'long_resp'= Long resp; 'miss_resp'= Missed resp; 'unbound_data_rcv'= Unbound data rcvd; 'pause_conn'= Pause request; 'pause_conn_fail'= Pause request fail; 'resume_conn'= Resume request; 'not_remove_from_rport'= Not remove from list;



  oper (False, any, None)
    Field oper


    connection_reuse_cpu_list (optional, any, None)
      Field connection_reuse_cpu_list


    cpu_count (optional, any, None)
      Field cpu_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    miss_resp (optional, any, None)
      Missed resp


    nunbind (optional, any, None)
      Total unbind


    ntermi_err (optional, any, None)
      Total terminated by err


    nbind (optional, any, None)
      Total bind


    current_active (optional, any, None)
      Active persist


    pause_conn_fail (optional, any, None)
      Pause request fail


    delay_unbind (optional, any, None)
      Delayed unbind


    long_resp (optional, any, None)
      Long resp


    ntermi (optional, any, None)
      Total terminated


    pause_conn (optional, any, None)
      Pause request


    unbound_data_rcv (optional, any, None)
      Unbound data rcvd


    resume_conn (optional, any, None)
      Resume request


    current_open (optional, any, None)
      Open persist


    not_remove_from_rport (optional, any, None)
      Not remove from list


    nestab (optional, any, None)
      Total established



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


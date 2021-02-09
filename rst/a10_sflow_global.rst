.. _a10_sflow_global_module:


a10_sflow_global -- Configures A10 sflow.global
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

sFlow global






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total-packet-sample-records'= Total packet sample records; 'total- counter-sample-records'= Total counter sample records; 'total-sflow-packets- sent'= Total sflow packets sent;



  oper (False, any, None)
    Field oper


    if_stats_list (optional, any, None)
      Field if_stats_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    total_packet_sample_records (optional, any, None)
      Total packet sample records


    total_counter_sample_records (optional, any, None)
      Total counter sample records


    total_sflow_packets_sent (optional, any, None)
      Total sflow packets sent



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


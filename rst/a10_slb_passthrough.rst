.. _a10_slb_passthrough_module:


a10_slb_passthrough -- Configures A10 slb.passthrough
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

passthrough session stats






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'curr_conn'= Current connections; 'total_conn'= Total connections; 'total_fwd_bytes'= Forward bytes; 'total_fwd_packets'= Forward packets; 'total_rev_bytes'= Reverse bytes; 'total_rev_packets'= Reverse packets; 'curr_pconn'= Persistent connections;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    curr_pconn (optional, any, None)
      Persistent connections


    total_fwd_packets (optional, any, None)
      Forward packets


    curr_conn (optional, any, None)
      Current connections


    total_rev_packets (optional, any, None)
      Reverse packets


    total_conn (optional, any, None)
      Total connections


    total_rev_bytes (optional, any, None)
      Reverse bytes


    total_fwd_bytes (optional, any, None)
      Forward bytes



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


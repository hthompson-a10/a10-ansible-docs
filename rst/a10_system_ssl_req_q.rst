.. _a10_system_ssl_req_q_module:


a10_system_ssl_req_q -- Configures A10 system.ssl-req-q
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

System SSL Request Queue statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'num-ssl-queues'= num-ssl-queues; 'ssl-req-q-depth-tot'= ssl-req-q- depth-tot; 'ssl-req-q-inuse-tot'= ssl-req-q-inuse-tot; 'ssl-hw-q-depth-tot'= ssl-hw-q-depth-tot; 'ssl-hw-q-inuse-tot'= ssl-hw-q-inuse-tot;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    ssl_req_q_depth_tot (optional, any, None)
      Field ssl_req_q_depth_tot


    ssl_req_q_inuse_tot (optional, any, None)
      Field ssl_req_q_inuse_tot


    num_ssl_queues (optional, any, None)
      Field num_ssl_queues


    ssl_hw_q_depth_tot (optional, any, None)
      Field ssl_hw_q_depth_tot


    ssl_hw_q_inuse_tot (optional, any, None)
      Field ssl_hw_q_inuse_tot



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


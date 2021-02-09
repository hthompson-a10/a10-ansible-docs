.. _a10_slb_rate_limit_log_module:


a10_slb_rate_limit_log -- Configures A10 slb.rate-limit-log
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure rate limit logging






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total_log_times'= Total log times; 'total_log_msg'= Total log messages; 'local_log_msg'= Local log messages; 'remote_log_msg'= Remote log messages; 'local_log_rate'= Local rate (per sec); 'remote_log_rate'= Remote rate (per sec); 'msg_too_big'= Log message too big; 'buff_alloc_fail'= Buffer alloc fail; 'no_route'= No route; 'buff_send_fail'= Buffer send fail; 'alloc_conn'= Log-session alloc; 'free_conn'= Log-session free; 'conn_alloc_fail'= Log-session alloc fail; 'no_repeat_msg'= No repeat message; 'local_log_dropped'= Local log dropped due to rate-limit;



  oper (False, any, None)
    Field oper


    rate_limit_log_cpu_list (optional, any, None)
      Field rate_limit_log_cpu_list


    cpu_count (optional, any, None)
      Field cpu_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    msg_too_big (optional, any, None)
      Log message too big


    buff_send_fail (optional, any, None)
      Buffer send fail


    total_log_times (optional, any, None)
      Total log times


    remote_log_rate (optional, any, None)
      Remote rate (per sec)


    total_log_msg (optional, any, None)
      Total log messages


    no_repeat_msg (optional, any, None)
      No repeat message


    free_conn (optional, any, None)
      Log-session free


    conn_alloc_fail (optional, any, None)
      Log-session alloc fail


    local_log_msg (optional, any, None)
      Local log messages


    local_log_dropped (optional, any, None)
      Local log dropped due to rate-limit


    alloc_conn (optional, any, None)
      Log-session alloc


    no_route (optional, any, None)
      No route


    remote_log_msg (optional, any, None)
      Remote log messages


    local_log_rate (optional, any, None)
      Local rate (per sec)


    buff_alloc_fail (optional, any, None)
      Buffer alloc fail



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


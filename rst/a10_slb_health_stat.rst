.. _a10_slb_health_stat_module:


a10_slb_health_stat -- Configures A10 slb.health-stat
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure health monitor






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'num_burst'= Number of burst; 'max_jiffie'= Maximum number of jiffies; 'min_jiffie'= Minimum number of jiffies; 'avg_jiffie'= Average number of jiffies; 'open_socket'= Number of open sockets; 'open_socket_failed'= Number of failed open sockets; 'close_socket'= Number of closed sockets; 'connect_failed'= Number of failed connections; 'send_packet'= Number of packets sent; 'send_packet_failed'= Number of packet send failures; 'recv_packet'= Number of received packets; 'recv_packet_failed'= Number of failed packet receives; 'retry_times'= Retry times; 'timeout'= Timouet value; 'unexpected_error'= Number of unexpected errors; 'conn_imdt_succ'= Number of connection immediete success; 'sock_close_before_17'= Number of sockets closed before l7; 'sock_close_without_notify'= Number of sockets closed without notify; 'curr_health_rate'= Current health rate; 'ext_health_rate'= External health rate; 'ext_health_rate_val'= External health rate value; 'total_number'= Total number; 'status_up'= Number of status ups; 'status_down'= Number of status downs; 'status_unkn'= Number of status unknowns; 'status_other'= Number of other status; 'running_time'= Running time; 'config_health_rate'= Config health rate;



  oper (False, any, None)
    Field oper


    health_check_list (optional, any, None)
      Field health_check_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    min_jiffie (optional, any, None)
      Minimum number of jiffies


    sock_close_before_17 (optional, any, None)
      Number of sockets closed before l7


    max_jiffie (optional, any, None)
      Maximum number of jiffies


    timeout (optional, any, None)
      Timouet value


    config_health_rate (optional, any, None)
      Config health rate


    close_socket (optional, any, None)
      Number of closed sockets


    num_burst (optional, any, None)
      Number of burst


    ext_health_rate_val (optional, any, None)
      External health rate value


    retry_times (optional, any, None)
      Retry times


    open_socket (optional, any, None)
      Number of open sockets


    conn_imdt_succ (optional, any, None)
      Number of connection immediete success


    avg_jiffie (optional, any, None)
      Average number of jiffies


    status_up (optional, any, None)
      Number of status ups


    status_other (optional, any, None)
      Number of other status


    unexpected_error (optional, any, None)
      Number of unexpected errors


    running_time (optional, any, None)
      Running time


    ext_health_rate (optional, any, None)
      External health rate


    status_unkn (optional, any, None)
      Number of status unknowns


    total_number (optional, any, None)
      Total number


    status_down (optional, any, None)
      Number of status downs


    recv_packet_failed (optional, any, None)
      Number of failed packet receives


    connect_failed (optional, any, None)
      Number of failed connections


    send_packet (optional, any, None)
      Number of packets sent


    recv_packet (optional, any, None)
      Number of received packets


    curr_health_rate (optional, any, None)
      Current health rate


    sock_close_without_notify (optional, any, None)
      Number of sockets closed without notify


    open_socket_failed (optional, any, None)
      Number of failed open sockets


    send_packet_failed (optional, any, None)
      Number of packet send failures



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


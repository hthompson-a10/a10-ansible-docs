.. _a10_slb_template_port_module:


a10_slb_template_port -- Configures A10 slb.template.port
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Port template






Parameters
----------

  bw_rate_limit_duration (False, any, None)
    Duration in seconds the observed rate needs to honor


  weight (False, any, None)
    Weight (port weight)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  dest_nat (False, any, None)
    Destination NAT


  initial_slow_start (False, any, None)
    Initial slow start connection limit (default 128)


  slow_start (False, any, None)
    Slowly ramp up the connection number after port is up


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  sub_group (False, any, None)
    Divide service group members into different sub groups (Sub group ID (default is 0))


  del_session_on_server_down (False, any, None)
    Delete session if the server/port goes down (either disabled/hm down)


  decrement (False, any, None)
    Decrease after every round of DNS query (default is 0)


  retry (False, any, None)
    Maximum retry times before reassign this connection to another server/port (default is 2) (The maximum retry number)


  flap_period (False, any, None)
    take service out of rotation if max-flaps exceeded within time in seconds


  uuid (False, any, None)
    uuid of the object


  request_rate_no_logging (False, any, None)
    Do not log connection over limit event


  extended_stats (False, any, None)
    Enable extended statistics on real server port


  ansible_host (True, any, None)
    Host for AXAPI authentication


  till (False, any, None)
    Slow start ends when slow start connection limit reaches a number (default 4096) (Slow start ends when connection limit reaches this number)


  template_port_pool_shared (False, any, None)
    Source NAT (IP NAT Pool or pool group name)


  conn_rate_limit_no_logging (False, any, None)
    Do not log connection over limit event


  conn_limit_no_logging (False, any, None)
    Do not log connection over limit event


  reset (False, any, None)
    Send client reset when connection rate over limit


  health_check (False, any, None)
    Health Check Monitor (Health monitor name)


  state (True, any, None)
    State of the object to be created.


  stats_data_action (False, any, None)
    'stats-data-enable'= Enable statistical data collection for real server port; 'stats-data-disable'= Disable statistical data collection for real server port;


  request_rate_limit (False, any, None)
    Request rate limit


  bw_rate_limit (False, any, None)
    Configure bandwidth rate limit on real server port (Bandwidth rate limit in Kbps)


  conn_limit (False, any, None)
    Connection limit


  add (False, any, None)
    Slow start connection limit add by a number every interval (Add by this number every interval)


  every (False, any, None)
    Slow start connection limit increment interval (default 10)


  dscp (False, any, None)
    Differentiated Services Code Point (DSCP to Real Server IP Mapping Value)


  down_timer (False, any, None)
    The timer to bring the marked down server/port to up (default is 0, never bring up) (The timer to bring up server (in second, default is 0))


  conn_rate_limit (False, any, None)
    Connection rate limit


  bw_rate_limit_no_logging (False, any, None)
    Do not log bandwidth rate limit related state transitions


  a10_partition (False, any, None)
    Destination/target partition for object/command


  source_nat (False, any, None)
    Source NAT (IP NAT Pool or pool group name)


  health_check_disable (False, any, None)
    Disable configured health check configuration


  dynamic_member_priority (False, any, None)
    Set dynamic member's priority (Initial priority (default is 16))


  resel_on_reset (False, any, None)
    When receiving reset from server, do the server/port reselection (default is 0, don't do reselection)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  no_ssl (False, any, None)
    No SSL


  name (True, any, None)
    Port template name


  dampening_flaps (False, any, None)
    service dampening flaps count (max-flaps allowed in flap period)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  restore_svc_time (False, any, None)
    put the service back to the rotation after time in seconds


  request_rate_interval (False, any, None)
    '100ms'= Use 100 ms as sampling interval; 'second'= Use 1 second as sampling interval;


  resume (False, any, None)
    Resume accepting new connection after connection number drops below threshold (Connection resume threshold)


  times (False, any, None)
    Slow start connection limit multiply by a number every interval (default 2) (Multiply by this number every interval)


  shared_partition_pool (False, any, None)
    Reference a NAT pool or pool-group from shared partition


  down_grace_period (False, any, None)
    Port down grace period (Down grace period in seconds)


  inband_health_check (False, any, None)
    Use inband traffic to detect port's health status


  bw_rate_limit_resume (False, any, None)
    Resume server selection after bandwidth drops below this threshold (in Kbps) (Bandwidth rate limit resume threshold (in Kbps))


  reassign (False, any, None)
    Maximum reassign times before declear the server/port down (default is 25) (The maximum reassign number)


  user_tag (False, any, None)
    Customized tag


  rate_interval (False, any, None)
    '100ms'= Use 100 ms as sampling interval; 'second'= Use 1 second as sampling interval;









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


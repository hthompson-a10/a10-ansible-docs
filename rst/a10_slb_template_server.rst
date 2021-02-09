.. _a10_slb_template_server_module:


a10_slb_template_server -- Configures A10 slb.template.server
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Server template






Parameters
----------

  bw_rate_limit_duration (False, any, None)
    Duration in seconds the observed rate needs to honor


  weight (False, any, None)
    Weight for the Real Servers (Connection Weight (default is 1))


  ansible_username (True, any, None)
    Username for AXAPI authentication


  initial_slow_start (False, any, None)
    Initial slow start connection limit (default 128)


  slow_start (False, any, None)
    Slowly ramp up the connection number after server is up


  spoofing_cache (False, any, None)
    Servers under the template are spoofing cache


  log_selection_failure (False, any, None)
    Enable real-time logging for server selection failure event


  conn_rate_limit (False, any, None)
    Connection rate limit


  uuid (False, any, None)
    uuid of the object


  dynamic_server_prefix (False, any, None)
    Prefix of dynamic server (Prefix of dynamic server (default is 'DRS'))


  min_ttl_ratio (False, any, None)
    Minimum TTL to DNS query interval ratio (Minimum TTL ratio (default is 2))


  extended_stats (False, any, None)
    Enable extended statistics on real server


  till (False, any, None)
    Slow start ends when slow start connection limit reaches a number (default 4096) (Slow start ends when connection limit reaches this number)


  state (True, any, None)
    State of the object to be created.


  conn_rate_limit_no_logging (False, any, None)
    Do not log connection over limit event


  conn_limit_no_logging (False, any, None)
    Do not log connection over limit event


  health_check (False, any, None)
    Health Check Monitor (Health monitor name)


  resume (False, any, None)
    Resume accepting new connection after connection number drops below threshold (Connection resume threshold)


  stats_data_action (False, any, None)
    'stats-data-enable'= Enable statistical data collection for real server; 'stats-data-disable'= Disable statistical data collection for real server;


  bw_rate_limit (False, any, None)
    Configure bandwidth rate limit on real server (Bandwidth rate limit in Kbps)


  conn_limit (False, any, None)
    Connection limit


  add (False, any, None)
    Slow start connection limit add by a number every interval (Add by this number every interval)


  max_dynamic_server (False, any, None)
    Maximum dynamic server number (Maximum dynamic server number (default is 255))


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  bw_rate_limit_no_logging (False, any, None)
    Do not log bandwidth rate limit related state transitions


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  health_check_disable (False, any, None)
    Disable configured health check configuration


  name (True, any, None)
    Server template name


  ansible_port (True, any, None)
    Port for AXAPI authentication


  dns_fail_interval (False, any, None)
    The interval to retry when DNS failed to query (DNS failure interval (in second, default is 30))


  dns_query_interval (False, any, None)
    The interval to query DNS server for the hostname (DNS query interval (in minute, default is 10))


  ansible_password (True, any, None)
    Password for AXAPI authentication


  times (False, any, None)
    Slow start connection limit multiply by a number every interval (default 2) (Multiply by this number every interval)


  bw_rate_limit_resume (False, any, None)
    Resume server selection after bandwidth drops below this threshold (in Kbps) (Bandwidth rate limit resume threshold (in Kbps))


  every (False, any, None)
    Slow start connection limit increment interval (default 10)


  bw_rate_limit_acct (False, any, None)
    'to-server-only'= Only account for traffic sent to server; 'from-server-only'= Only account for traffic received from server; 'all'= Account for all traffic sent to and received from server;


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


.. _a10_acos_events_collector_group_module:


a10_acos_events_collector_group -- Configures A10 acos-events.collector-group
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure log servers group






Parameters
----------

  health_check (False, any, None)
    Health Check (Monitor Name)


  protocol (False, any, None)
    'udp'= use udp syslog protocol to send messages to log collector; 'tcp'= use tcp syslog protocol to send messages to log collector;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  facility (False, any, None)
    'local0'= Local use(Default); 'local1'= Local use; 'local2'= Local use; 'local3'= Local use; 'local4'= Local use; 'local5'= Local use; 'local6'= Local use; 'local7'= Local use;  (Facility parameter for syslog messages)


  rate (False, any, None)
    Specify the log message rate per second(Default 500)


  use_mgmt_port (False, any, None)
    Use managament port to connect to the log servers


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'msgs_sent'= Number of log messages sent; 'msgs_rate_limited'= Number of rate limited log messages; 'msgs_dropped'= Number of messages dropped for other reasons;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    msgs_rate_limited (optional, any, None)
      Number of rate limited log messages


    name (optional, any, None)
      Specify log server group name


    msgs_sent (optional, any, None)
      Number of log messages sent


    msgs_dropped (optional, any, None)
      Number of messages dropped for other reasons



  name (True, any, None)
    Specify log server group name


  log_server_list (False, any, None)
    Field log_server_list


    port (optional, any, None)
      Port number


    uuid (optional, any, None)
      uuid of the object


    name (optional, any, None)
      Member name



  user_tag (False, any, None)
    Customized tag


  format (False, any, None)
    'syslog'= log message format is syslog (Default); 'cef'= log message format is cef; 'leef'= log message format is leef;


  state (True, any, None)
    State of the object to be created.


  ansible_password (True, any, None)
    Password for AXAPI authentication









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


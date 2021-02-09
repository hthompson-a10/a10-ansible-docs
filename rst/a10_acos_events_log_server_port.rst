.. _a10_acos_events_log_server_port_module:


a10_acos_events_log_server_port -- Configures A10 acos-events.log.server.port
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Logging Server Port






Parameters
----------

  health_check (False, any, None)
    Health Check (Monitor Name)


  protocol (True, any, None)
    'tcp'= TCP Port; 'udp'= UDP Port;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  port_number (True, any, None)
    Port Number


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  health_check_disable (False, any, None)
    Disable health check


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'msgs_sent'= Number of log messages sent;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    port_number (optional, any, None)
      Port Number


    protocol (optional, any, None)
      'tcp'= TCP Port; 'udp'= UDP Port;


    msgs_sent (optional, any, None)
      Number of log messages sent



  uuid (False, any, None)
    uuid of the object


  log_server_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'enable'= enable; 'disable'= disable;


  user_tag (False, any, None)
    Customized tag









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


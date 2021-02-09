.. _a10_acos_events_log_server_module:


a10_acos_events_log_server -- Configures A10 acos-events.log-server
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Acos logging Server






Parameters
----------

  health_check (False, any, None)
    Health Check Monitor (Health monitor name)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  resolve_as (False, any, None)
    'resolve-to-ipv4'= Use A Query only to resolve FQDN; 'resolve-to-ipv6'= Use AAAA Query only to resolve FQDN; 'resolve-to-ipv4-and-ipv6'= Use A as well as AAAA Query to resolve FQDN;


  host (False, any, None)
    IP Address


  port_list (False, any, None)
    Field port_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    health_check (optional, any, None)
      Health Check (Monitor Name)


    protocol (optional, any, None)
      'tcp'= TCP Port; 'udp'= UDP Port;


    uuid (optional, any, None)
      uuid of the object


    port_number (optional, any, None)
      Port Number


    action (optional, any, None)
      'enable'= enable; 'disable'= disable;


    user_tag (optional, any, None)
      Customized tag


    health_check_disable (optional, any, None)
      Disable health check



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  health_check_disable (False, any, None)
    Disable configured health check configuration


  uuid (False, any, None)
    uuid of the object


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'msgs_sent'= Number of log messages sent;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    name (optional, any, None)
      Server Name


    msgs_sent (optional, any, None)
      Number of log messages sent


    port_list (optional, any, None)
      Field port_list



  name (True, any, None)
    Server Name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'enable'= Enable this Logging Server; 'disable'= Disable this Logging Server;


  user_tag (False, any, None)
    Customized tag


  server_ipv6_addr (False, any, None)
    IPV6 address









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


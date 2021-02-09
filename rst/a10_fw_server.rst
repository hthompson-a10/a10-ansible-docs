.. _a10_fw_server_module:


a10_fw_server -- Configures A10 fw.server
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Firewall logging Server






Parameters
----------

  oper (False, any, None)
    Field oper


    state (optional, any, None)
      Field state


    name (optional, any, None)
      Server Name


    port_list (optional, any, None)
      Field port_list



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


  stats (False, any, None)
    Field stats


    curr_conn (optional, any, None)
      Current connections


    name (optional, any, None)
      Server Name


    peak_conn (optional, any, None)
      Peak connections


    rev_pkt (optional, any, None)
      Reverse Packets


    total_conn (optional, any, None)
      Total connections


    fwd_pkt (optional, any, None)
      Forward packets


    port_list (optional, any, None)
      Field port_list



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
      'all'= all; 'curr-conn'= Current connections; 'total-conn'= Total connections; 'fwd-pkt'= Forward packets; 'rev-pkt'= Reverse Packets; 'peak-conn'= Peak connections;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  fqdn_name (False, any, None)
    Server hostname


  name (True, any, None)
    Server Name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'enable'= Enable this Real Server; 'disable'= Disable this Real Server;


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


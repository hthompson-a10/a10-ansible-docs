.. _a10_gslb_service_ip_port_module:


a10_gslb_service_ip_port -- Configures A10 gslb.service.ip.port
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Server Port






Parameters
----------

  service_ip_node_name (optional, any, None)
    Key to identify parent object


  oper (False, any, None)
    Field oper


    use_gslb_state (optional, any, None)
      Field use_gslb_state


    local_protocol (optional, any, None)
      Field local_protocol


    service_port (optional, any, None)
      Field service_port


    dynamic (optional, any, None)
      Field dynamic


    tcp (optional, any, None)
      Field tcp


    disabled (optional, any, None)
      Field disabled


    state (optional, any, None)
      Field state


    manually_health_check (optional, any, None)
      Field manually_health_check


    port_num (optional, any, None)
      Port Number


    gslb_protocol (optional, any, None)
      Field gslb_protocol


    port_proto (optional, any, None)
      'tcp'= TCP Port; 'udp'= UDP Port;



  health_check (False, any, None)
    Health Check Monitor (Monitor Name)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  health_check_protocol_disable (False, any, None)
    Disable GSLB Protocol Health Monitor


  a10_partition (False, any, None)
    Destination/target partition for object/command


  follow_port_protocol (False, any, None)
    'tcp'= TCP Port; 'udp'= UDP Port;


  health_check_disable (False, any, None)
    Disable Health Check Monitor


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'active'= Active Servers; 'current'= Current Connections;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    active (optional, any, None)
      Active Servers


    current (optional, any, None)
      Current Connections


    port_num (optional, any, None)
      Port Number


    port_proto (optional, any, None)
      'tcp'= TCP Port; 'udp'= UDP Port;



  uuid (False, any, None)
    uuid of the object


  user_tag (False, any, None)
    Customized tag


  port_num (True, any, None)
    Port Number


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'enable'= Enable this GSLB server port; 'disable'= Disable this GSLB server port;


  port_proto (True, any, None)
    'tcp'= TCP Port; 'udp'= UDP Port;


  health_check_follow_port (False, any, None)
    Specify which port to follow for health status (Port Number)









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


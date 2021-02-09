.. _a10_gslb_service_ip_module:


a10_gslb_service_ip -- Configures A10 gslb.service-ip
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Service IP






Parameters
----------

  oper (False, any, None)
    Field oper


    use_gslb_state (optional, any, None)
      Field use_gslb_state


    local_protocol (optional, any, None)
      Field local_protocol


    ip (optional, any, None)
      Field ip


    port_count (optional, any, None)
      Field port_count


    dynamic (optional, any, None)
      Field dynamic


    service_ip (optional, any, None)
      Field service_ip


    node_name (optional, any, None)
      Service-IP Name


    disabled (optional, any, None)
      Field disabled


    state (optional, any, None)
      Field state


    manually_health_check (optional, any, None)
      Field manually_health_check


    port_list (optional, any, None)
      Field port_list


    gslb_protocol (optional, any, None)
      Field gslb_protocol


    virtual_server (optional, any, None)
      Field virtual_server



  ipv6_address (False, any, None)
    IPV6 address


  health_check (False, any, None)
    Health Check Monitor (Monitor Name)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  port_list (False, any, None)
    Field port_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    health_check (optional, any, None)
      Health Check Monitor (Monitor Name)


    uuid (optional, any, None)
      uuid of the object


    port_proto (optional, any, None)
      'tcp'= TCP Port; 'udp'= UDP Port;


    port_num (optional, any, None)
      Port Number


    health_check_follow_port (optional, any, None)
      Specify which port to follow for health status (Port Number)


    action (optional, any, None)
      'enable'= Enable this GSLB server port; 'disable'= Disable this GSLB server port;


    health_check_protocol_disable (optional, any, None)
      Disable GSLB Protocol Health Monitor


    user_tag (optional, any, None)
      Customized tag


    follow_port_protocol (optional, any, None)
      'tcp'= TCP Port; 'udp'= UDP Port;


    health_check_disable (optional, any, None)
      Disable Health Check Monitor



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  health_check_protocol_disable (False, any, None)
    Disable GSLB Protocol Health Monitor


  ip_address (False, any, None)
    IP address


  ansible_host (True, any, None)
    Host for AXAPI authentication


  health_check_disable (False, any, None)
    Disable Health Check Monitor


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hits'= Number of times the service IP has been selected; 'recent'= Recent hits;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    hits (optional, any, None)
      Number of times the service IP has been selected


    recent (optional, any, None)
      Recent hits


    port_list (optional, any, None)
      Field port_list


    node_name (optional, any, None)
      Service-IP Name



  uuid (False, any, None)
    uuid of the object


  external_ip (False, any, None)
    External IP address for NAT


  a10_partition (False, any, None)
    Destination/target partition for object/command


  user_tag (False, any, None)
    Customized tag


  node_name (True, any, None)
    Service-IP Name


  state (True, any, None)
    State of the object to be created.


  ipv6 (False, any, None)
    IPv6 address Mapping (Applicable only when service-ip has an IPv4 Address)


  action (False, any, None)
    'enable'= Enable this GSLB server; 'disable'= Disable this GSLB server;


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


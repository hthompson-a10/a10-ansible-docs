.. _a10_interface_management_module:


a10_interface_management -- Configures A10 interface.management
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Management interface






Parameters
----------

  oper (False, any, None)
    Field oper


    ipv6_addr (optional, any, None)
      Field ipv6_addr


    line_protocol (optional, any, None)
      Field line_protocol


    ipv6_acl (optional, any, None)
      Field ipv6_acl


    ipv4_default_gateway (optional, any, None)
      IP gateway address


    mac (optional, any, None)
      Field mac


    ipv4_addr (optional, any, None)
      IP address


    interface (optional, any, None)
      Field interface


    link_type (optional, any, None)
      Field link_type


    dhcp_enabled (optional, any, None)
      Field dhcp_enabled


    speed (optional, any, None)
      Field speed


    ipv4_acl (optional, any, None)
      Field ipv4_acl


    ipv6_link_local (optional, any, None)
      Field ipv6_link_local


    duplexity (optional, any, None)
      Field duplexity


    ipv6_link_local_prefix (optional, any, None)
      Field ipv6_link_local_prefix


    mtu (optional, any, None)
      Field mtu


    state (optional, any, None)
      Field state


    ipv4_mask (optional, any, None)
      IP subnet mask


    flow_control (optional, any, None)
      Field flow_control


    ipv6_prefix (optional, any, None)
      Field ipv6_prefix


    ipv6_default_gateway (optional, any, None)
      Field ipv6_default_gateway



  lldp (False, any, None)
    Field lldp


    enable_cfg (optional, any, None)
      Field enable_cfg


    tx_dot1_cfg (optional, any, None)
      Field tx_dot1_cfg


    notification_cfg (optional, any, None)
      Field notification_cfg


    tx_tlvs_cfg (optional, any, None)
      Field tx_tlvs_cfg


    uuid (optional, any, None)
      uuid of the object



  secondary_ip (False, any, None)
    Field secondary_ip


    ipv4_address (optional, any, None)
      IP address


    ipv4_netmask (optional, any, None)
      IP subnet mask


    secondary_ip (optional, any, None)
      Global IP configuration subcommands


    default_gateway (optional, any, None)
      Set default gateway (Default gateway address)


    dhcp (optional, any, None)
      Use DHCP to configure IP address


    control_apps_use_mgmt_port (optional, any, None)
      Control applications use management port



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip (False, any, None)
    Field ip


    ipv4_address (optional, any, None)
      IP address


    dhcp (optional, any, None)
      Use DHCP to configure IP address


    ipv4_netmask (optional, any, None)
      IP subnet mask


    control_apps_use_mgmt_port (optional, any, None)
      Control applications use management port


    default_gateway (optional, any, None)
      Set default gateway (Default gateway address)



  broadcast_rate_limit (False, any, None)
    Field broadcast_rate_limit


    rate (optional, any, None)
      packets per second. Default is 500. (packets per second. Please specify an even number. Default is 500)


    bcast_rate_limit_enable (optional, any, None)
      Rate limit the l2 broadcast packet on mgmt port



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'packets_input'= Input packets; 'bytes_input'= Input bytes; 'received_broadcasts'= Received broadcasts; 'received_multicasts'= Received multicasts; 'received_unicasts'= Received unicasts; 'input_errors'= Input errors; 'crc'= CRC; 'frame'= Frames; 'input_err_short'= Runts; 'input_err_long'= Giants; 'packets_output'= Output packets; 'bytes_output'= Output bytes; 'transmitted_broadcasts'= Transmitted broadcasts; 'transmitted_multicasts'= Transmitted multicasts; 'transmitted_unicasts'= Transmitted unicasts; 'output_errors'= Output errors; 'collisions'= Collisions;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    received_broadcasts (optional, any, None)
      Received broadcasts


    frame (optional, any, None)
      Frames


    bytes_output (optional, any, None)
      Output bytes


    collisions (optional, any, None)
      Collisions


    input_errors (optional, any, None)
      Input errors


    bytes_input (optional, any, None)
      Input bytes


    transmitted_broadcasts (optional, any, None)
      Transmitted broadcasts


    transmitted_multicasts (optional, any, None)
      Transmitted multicasts


    packets_input (optional, any, None)
      Input packets


    input_err_short (optional, any, None)
      Runts


    received_multicasts (optional, any, None)
      Received multicasts


    packets_output (optional, any, None)
      Output packets


    transmitted_unicasts (optional, any, None)
      Transmitted unicasts


    input_err_long (optional, any, None)
      Giants


    crc (optional, any, None)
      CRC


    received_unicasts (optional, any, None)
      Received unicasts


    output_errors (optional, any, None)
      Output errors



  uuid (False, any, None)
    uuid of the object


  duplexity (False, any, None)
    'Full'= Full; 'Half'= Half; 'auto'= Auto;


  speed (False, any, None)
    '10'= 10 Mbs/sec; '100'= 100 Mbs/sec; '1000'= 1 Gb/sec; 'auto'= Auto Negotiate Speed;  (Interface Speed)


  access_list (False, any, None)
    Field access_list


    acl_id (optional, any, None)
      ACL id


    acl_name (optional, any, None)
      Apply an access list (Named Access List)



  state (True, any, None)
    State of the object to be created.


  flow_control (False, any, None)
    Enable 802.3x flow control on full duplex port


  ipv6 (False, any, None)
    Field ipv6


    inbound (optional, any, None)
      ACL applied on incoming packets to this interface


    ipv6_addr (optional, any, None)
      Set the IPv6 address of an interface


    address_type (optional, any, None)
      'link-local'= Configure an IPv6 link local address;


    v6_acl_name (optional, any, None)
      Apply ACL rules to incoming packets on this interface (Named Access List)


    default_ipv6_gateway (optional, any, None)
      Set default gateway (Default gateway address)



  action (False, any, None)
    'enable'= Enable Management Port; 'disable'= Disable Management Port;


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


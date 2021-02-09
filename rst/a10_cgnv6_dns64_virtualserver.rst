.. _a10_cgnv6_dns64_virtualserver_module:


a10_cgnv6_dns64_virtualserver -- Configures A10 cgnv6.dns64-virtualserver
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create a DNS64 Virtual Server






Parameters
----------

  oper (False, any, None)
    Field oper


    migration_status (optional, any, None)
      Field migration_status


    peak_conn (optional, any, None)
      Field peak_conn


    ip_only_lb_fwd_pkts (optional, any, None)
      Field ip_only_lb_fwd_pkts


    ip_only_lb_fwd_bytes (optional, any, None)
      Field ip_only_lb_fwd_bytes


    curr_conn_rate (optional, any, None)
      Field curr_conn_rate


    mac (optional, any, None)
      Field mac


    port_list (optional, any, None)
      Field port_list


    curr_icmpv6_rate (optional, any, None)
      Field curr_icmpv6_rate


    ip_address (optional, any, None)
      Field ip_address


    name (optional, any, None)
      CGNV6 Virtual Server Name


    icmpv6_rate_over_limit_drop (optional, any, None)
      Field icmpv6_rate_over_limit_drop


    icmp_lockup_time_left (optional, any, None)
      Field icmp_lockup_time_left


    conn_rate_unit (optional, any, None)
      Field conn_rate_unit


    icmp_rate_over_limit_drop (optional, any, None)
      Field icmp_rate_over_limit_drop


    state (optional, any, None)
      Field state


    ip_only_lb_rev_bytes (optional, any, None)
      Field ip_only_lb_rev_bytes


    curr_conn_overflow (optional, any, None)
      Field curr_conn_overflow


    curr_icmp_rate (optional, any, None)
      Field curr_icmp_rate


    ip_only_lb_rev_pkts (optional, any, None)
      Field ip_only_lb_rev_pkts


    icmpv6_lockup_time_left (optional, any, None)
      Field icmpv6_lockup_time_left



  ipv6_address (False, any, None)
    IPV6 address


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  netmask (False, any, None)
    IP subnet mask


  template_policy (False, any, None)
    Policy template name


  port_list (False, any, None)
    Field port_list


    service_group (optional, any, None)
      Bind a Service Group to this Virtual Server (Service Group Name)


    sampling_enable (optional, any, None)
      Field sampling_enable


    protocol (optional, any, None)
      'dns-udp'= DNS service over UDP;


    uuid (optional, any, None)
      uuid of the object


    precedence (optional, any, None)
      Set auto NAT pool as higher precedence for source NAT


    auto (optional, any, None)
      Configure auto NAT for the vport


    acl_name_list (optional, any, None)
      Field acl_name_list


    template_dns (optional, any, None)
      DNS template (DNS template name)


    port_number (optional, any, None)
      Port


    template_policy (optional, any, None)
      Policy Template (Policy template name)


    action (optional, any, None)
      'enable'= Enable; 'disable'= Disable;


    acl_id_list (optional, any, None)
      Field acl_id_list


    user_tag (optional, any, None)
      Customized tag


    pool (optional, any, None)
      Specify NAT pool or pool group



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  use_if_ip (False, any, None)
    Use Interface IP


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    CGNV6 Virtual Server Name


  ip_address (False, any, None)
    IP Address


  vrid (False, any, None)
    Join a vrrp group (Specify ha VRRP-A vrid)


  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


  policy (False, any, None)
    Policy template


  ethernet (False, any, None)
    Ethernet interface


  enable_disable_action (False, any, None)
    'enable'= Enable Virtual Server (default); 'disable'= Disable Virtual Server;









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


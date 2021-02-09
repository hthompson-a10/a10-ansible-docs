.. _a10_snmp_server_enable_traps_module:


a10_snmp_server_enable_traps -- Configures A10 snmp.server.enable.traps
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable SNMP traps






Parameters
----------

  all (False, any, None)
    Enable all SNMP traps


  ansible_username (True, any, None)
    Username for AXAPI authentication


  lsn (False, any, None)
    Field lsn


    all (optional, any, None)
      Enable all LSN group traps


    uuid (optional, any, None)
      uuid of the object


    per_ip_port_usage_threshold (optional, any, None)
      Enable LSN trap when IP total port usage reaches the threshold (default 64512)


    total_port_usage_threshold (optional, any, None)
      Enable LSN trap when NAT total port usage reaches the threshold (default 655350000)


    fixed_nat_port_mapping_file_change (optional, any, None)
      Enable LSN trap when fixed nat port mapping file change


    max_port_threshold (optional, any, None)
      Maximum threshold


    max_ipport_threshold (optional, any, None)
      Maximum threshold


    traffic_exceeded (optional, any, None)
      Enable LSN trap when NAT pool reaches the threshold



  slb_change (False, any, None)
    Field slb_change


    ssl_cert_expire (optional, any, None)
      Enable SSL certificate expiring trap


    all (optional, any, None)
      Enable all system group traps


    ssl_cert_change (optional, any, None)
      Enable SSL certificate change trap


    connection_resource_event (optional, any, None)
      Enable system connection resource event trap


    resource_usage_warning (optional, any, None)
      Enable partition resource usage warning trap


    server (optional, any, None)
      Enable slb server create/delete trap


    vip (optional, any, None)
      Enable slb vip create/delete trap


    server_port (optional, any, None)
      Enable slb server port create/delete trap


    system_threshold (optional, any, None)
      Enable slb system threshold trap


    vip_port (optional, any, None)
      Enable slb vip-port create/delete trap


    uuid (optional, any, None)
      uuid of the object



  vrrp_a (False, any, None)
    Field vrrp_a


    active (optional, any, None)
      Enable VRRP-A active trap


    standby (optional, any, None)
      Enable VRRP-A standby trap


    all (optional, any, None)
      Enable all VRRP-A group traps


    uuid (optional, any, None)
      uuid of the object



  ssl (False, any, None)
    Field ssl


    uuid (optional, any, None)
      uuid of the object


    server_certificate_error (optional, any, None)
      Enable SSL server certificate error trap



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  network (False, any, None)
    Field network


    trunk_port_threshold (optional, any, None)
      Enable network trunk-port-threshold trap


    uuid (optional, any, None)
      uuid of the object



  lldp (False, any, None)
    Enable lldp traps


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  gslb (False, any, None)
    Field gslb


    all (optional, any, None)
      Enable all GSLB traps


    group (optional, any, None)
      Enable GSLB group related traps


    uuid (optional, any, None)
      uuid of the object


    zone (optional, any, None)
      Enable GSLB zone related traps


    site (optional, any, None)
      Enable GSLB site related traps


    service_ip (optional, any, None)
      Enable GSLB service-ip related traps



  snmp (False, any, None)
    Field snmp


    linkup (optional, any, None)
      Enable SNMP link-up trap


    all (optional, any, None)
      Enable all SNMP group traps


    linkdown (optional, any, None)
      Enable SNMP link-down trap


    uuid (optional, any, None)
      uuid of the object



  system (False, any, None)
    Field system


    smp_resource_event (optional, any, None)
      Enable system smp resource event trap


    sec_disk (optional, any, None)
      Enable system secondary hard disk trap


    all (optional, any, None)
      Enable all system group traps


    low_temp (optional, any, None)
      Enable system low temperature trap


    high_memory_use (optional, any, None)
      Enable system high memory usage trap


    power (optional, any, None)
      Enable system power supply trap


    high_temp (optional, any, None)
      Enable system high temperature trap


    tacacs_server_up_down (optional, any, None)
      Enable system TACACS monitor server up/down trap


    file_sys_read_only (optional, any, None)
      Enable file system read-only trap


    fan (optional, any, None)
      Enable system fan trap


    shutdown (optional, any, None)
      Enable system shutdown trap


    control_cpu_high (optional, any, None)
      Enable control CPU usage high trap


    syslog_severity_one (optional, any, None)
      Enable system syslog severity one messages trap


    restart (optional, any, None)
      Enable system restart trap


    packet_drop (optional, any, None)
      Enable system packet dropped trap


    uuid (optional, any, None)
      uuid of the object


    license_management (optional, any, None)
      Enable system license management traps


    high_disk_use (optional, any, None)
      Enable system high disk usage trap


    start (optional, any, None)
      Enable system start trap


    data_cpu_high (optional, any, None)
      Enable data CPU usage high trap


    pri_disk (optional, any, None)
      Enable system primary hard disk trap



  state (True, any, None)
    State of the object to be created.


  vcs (False, any, None)
    Field vcs


    state_change (optional, any, None)
      Enable VCS state change trap


    uuid (optional, any, None)
      uuid of the object



  routing (False, any, None)
    Field routing


    bgp (optional, any, None)
      Field bgp


    isis (optional, any, None)
      Field isis


    ospf (optional, any, None)
      Field ospf



  ansible_password (True, any, None)
    Password for AXAPI authentication


  slb (False, any, None)
    Field slb


    service_group_member_up (optional, any, None)
      Enable SLB service-group-member-up trap


    all (optional, any, None)
      Enable all SLB traps


    vip_port_connratelimit (optional, any, None)
      Enable the virtual port reach conn-rate-limit trap


    server_conn_resume (optional, any, None)
      Enable SLB server connection resume trap


    server_selection_failure (optional, any, None)
      Enable SLB server selection failure trap


    vip_connlimit (optional, any, None)
      Enable the virtual server reach conn-limit trap


    bw_rate_limit_exceed (optional, any, None)
      Enable SLB server/port bandwidth rate limit exceed trap


    server_down (optional, any, None)
      Enable SLB server-down trap


    service_group_up (optional, any, None)
      Enable SLB service-group-up trap


    vip_connratelimit (optional, any, None)
      Enable the virtual server reach conn-rate-limit trap


    vip_port_down (optional, any, None)
      Enable SLB virtual port down trap


    service_down (optional, any, None)
      Enable SLB service-down trap


    vip_port_connlimit (optional, any, None)
      Enable the virtual port reach conn-limit trap


    service_group_down (optional, any, None)
      Enable SLB service-group-down trap


    vip_up (optional, any, None)
      Enable SLB virtual server up trap


    vip_port_up (optional, any, None)
      Enable SLB virtual port up trap


    uuid (optional, any, None)
      uuid of the object


    gateway_up (optional, any, None)
      Enable SLB server gateway up trap


    service_conn_limit (optional, any, None)
      Enable SLB service connection limit trap


    gateway_down (optional, any, None)
      Enable SLB server gateway down trap


    service_group_member_down (optional, any, None)
      Enable SLB service-group-member-down trap


    vip_down (optional, any, None)
      Enable SLB virtual server down trap


    server_up (optional, any, None)
      Enable slb server up trap


    application_buffer_limit (optional, any, None)
      Enable application buffer reach limit trap


    bw_rate_limit_resume (optional, any, None)
      Enable SLB server/port bandwidth rate limit resume trap


    server_conn_limit (optional, any, None)
      Enable SLB server connection limit trap


    service_up (optional, any, None)
      Enable SLB service-up trap


    server_disabled (optional, any, None)
      Enable SLB server-disabled trap


    service_conn_resume (optional, any, None)
      Enable SLB service connection resume trap










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


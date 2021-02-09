.. _a10_slb_template_virtual_port_module:


a10_slb_template_virtual_port -- Configures A10 slb.template.virtual-port
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Virtual port template






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  allow_syn_otherflags (False, any, None)
    Allow initial SYN packet with other flags


  reset_l7_on_failover (False, any, None)
    Send reset to L7 client and server connection upon a failover


  reset_unknown_conn (False, any, None)
    Send reset back if receives TCP packet without SYN or RST flag and it does not belong to any existing connections


  rate (False, any, None)
    Source IP and port rate limit (Packet rate limit)


  pkt_rate_type (False, any, None)
    'src-ip-port'= Source IP and port rate limit; 'src-port'= Source port rate limit;


  aflow (False, any, None)
    Use aFlow to eliminate the traffic surge


  conn_rate_limit (False, any, None)
    Connection rate limit


  snat_msl (False, any, None)
    Source NAT MSL (Source NAT MSL value (seconds))


  ansible_host (True, any, None)
    Host for AXAPI authentication


  non_syn_initiation (False, any, None)
    Allow initial TCP packet to be non-SYN


  state (True, any, None)
    State of the object to be created.


  drop_unknown_conn (False, any, None)
    Drop conection if receives TCP packet without SYN or RST flag and it does not belong to any existing connections


  allow_vip_to_rport_mapping (False, any, None)
    Allow mapping of VIP to real port


  conn_rate_limit_no_logging (False, any, None)
    Do not log connection over limit event


  conn_limit_no_logging (False, any, None)
    Do not log connection over limit event


  when_rr_enable (False, any, None)
    Only do rate limit if CPU RR triggered


  snat_port_preserve (False, any, None)
    Source NAT Port Preservation


  ignore_tcp_msl (False, any, None)
    reclaim TCP resource immediately without MSL


  dscp (False, any, None)
    Differentiated Services Code Point (DSCP to Real Server IP Mapping Value)


  conn_limit (False, any, None)
    Connection limit


  conn_limit_reset (False, any, None)
    Send client reset when connection over limit


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  log_options (False, any, None)
    'no-logging'= Do not log over limit event; 'no-repeat-logging'= log once for over limit event. Default is log once per minute;


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Virtual port template name


  pkt_rate_limit_reset (False, any, None)
    send client-side reset (reset after packet limit)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  pkt_rate_interval (False, any, None)
    '100ms'= Source IP and port rate limit per 100ms; 'second'= Source IP and port rate limit per second (default);


  conn_rate_limit_reset (False, any, None)
    Send client reset when connection rate over limit


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


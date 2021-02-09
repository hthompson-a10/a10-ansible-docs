.. _a10_slb_template_virtual_server_module:


a10_slb_template_virtual_server -- Configures A10 slb.template.virtual-server
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Virtual server template






Parameters
----------

  subnet_gratuitous_arp (False, any, None)
    Send gratuitous ARP for every IP in the subnet virtual server


  ansible_username (True, any, None)
    Username for AXAPI authentication


  tcp_stack_tfo_backoff_time (False, any, None)
    The time tcp stack will wait before allowing new fast-open requests after security condition, default 600 seconds (number)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  conn_limit (False, any, None)
    Connection limit


  icmp_lockup_period (False, any, None)
    Lockup period (second)


  tcp_stack_tfo_active_conn_limit (False, any, None)
    The allowed active layer 7 tcp fast-open connection limit, default is zero (number)


  conn_limit_reset (False, any, None)
    Send client reset when connection over limit


  icmp_lockup (False, any, None)
    Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  icmpv6_lockup_period (False, any, None)
    Lockup period (second)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  icmp_rate_limit (False, any, None)
    ICMP rate limit (Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  conn_rate_limit (False, any, None)
    Connection rate limit


  uuid (False, any, None)
    uuid of the object


  icmpv6_rate_limit (False, any, None)
    ICMPv6 rate limit (Normal rate limit. If exceeds this limit, drop the ICMP packet that goes over the limit)


  name (True, any, None)
    Virtual server template name


  state (True, any, None)
    State of the object to be created.


  rate_interval (False, any, None)
    '100ms'= Use 100 ms as sampling interval; 'second'= Use 1 second as sampling interval;


  tcp_stack_tfo_cookie_time_limit (False, any, None)
    The time limit (in seconds) that a layer 7 tcp fast-open cookie is valid, default is 60 seconds (number)


  icmpv6_lockup (False, any, None)
    Enter lockup state when ICMP rate exceeds lockup rate limit (Maximum rate limit. If exceeds this limit, drop all ICMP packet for a time period)


  conn_rate_limit_reset (False, any, None)
    Send client reset when connection rate over limit


  conn_rate_limit_no_logging (False, any, None)
    Do not log connection over limit event


  user_tag (False, any, None)
    Customized tag


  conn_limit_no_logging (False, any, None)
    Do not log connection over limit event









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


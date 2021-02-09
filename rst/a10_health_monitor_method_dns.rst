.. _a10_health_monitor_method_dns_module:


a10_health_monitor_method_dns -- Configures A10 health.monitor.method.dns
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DNS type






Parameters
----------

  dns_domain_recurse (False, any, None)
    'enabled'= Set the recursion bit; 'disabled'= Clear the recursion bit;


  dns_ipv6_port (False, any, None)
    Specify DNS port, default is 53 (DNS Port(default 53))


  dns_ipv6_recurse (False, any, None)
    'enabled'= Set the recursion bit; 'disabled'= Clear the recursion bit;


  dns_ipv6_addr (False, any, None)
    Specify IPv6 address


  ansible_username (True, any, None)
    Username for AXAPI authentication


  dns_ipv4_expect (False, any, None)
    Field dns_ipv4_expect


    dns_ipv4_response (optional, any, None)
      Specify response code range (e.g. 0,1-5) (Format is xx,xx-xx (xx between [0,15]))



  dns_ipv6_expect (False, any, None)
    Field dns_ipv6_expect


    dns_ipv6_response (optional, any, None)
      Specify response code range (e.g. 0,1-5) (Format is xx,xx-xx (xx between [0,15]))



  dns_domain (False, any, None)
    Specify fully qualified domain name of the host


  dns_ipv6_tcp (False, any, None)
    Configure DNS transport over TCP, default is UDP


  dns_ipv4_addr (False, any, None)
    Specify IPv4 address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  dns_domain_type (False, any, None)
    'A'= Used for storing Ipv4 address (default); 'CNAME'= Canonical name for a DNS alias; 'SOA'= Start of authority; 'PTR'= Domain name pointer; 'MX'= Mail exchanger; 'TXT'= Text string; 'AAAA'= Used for storing Ipv6 128-bits address;


  dns_ipv4_recurse (False, any, None)
    'enabled'= Set the recursion bit; 'disabled'= Clear the recursion bit;


  dns_ipv4_port (False, any, None)
    Specify DNS port, default is 53 (DNS Port(default 53))


  monitor_name (optional, any, None)
    Key to identify parent object


  ansible_host (True, any, None)
    Host for AXAPI authentication


  dns_ipv4_tcp (False, any, None)
    Configure DNS transport over TCP, default is UDP


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  dns_domain_port (False, any, None)
    Specify DNS port, default is 53 (DNS Port(default 53))


  a10_partition (False, any, None)
    Destination/target partition for object/command


  state (True, any, None)
    State of the object to be created.


  dns_ip_key (False, any, None)
    Reverse DNS lookup (Specify IPv4 or IPv6 address)


  dns_domain_tcp (False, any, None)
    Configure DNS transport over TCP, default is UDP


  dns (False, any, None)
    DNS type


  ansible_password (True, any, None)
    Password for AXAPI authentication


  dns_domain_expect (False, any, None)
    Field dns_domain_expect


    dns_domain_response (optional, any, None)
      Specify response code range (e.g. 0,1-5) (Format is xx,xx-xx (xx between [0,15]))










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


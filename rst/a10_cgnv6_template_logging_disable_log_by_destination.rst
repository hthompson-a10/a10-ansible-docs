.. _a10_cgnv6_template_logging_disable_log_by_destination_module:


a10_cgnv6_template_logging_disable_log_by_destination -- Configures A10 cgnv6.template.logging.disable-log-by-destination
=========================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Disable logging by destination ip address protocol and port






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ip6_list (False, any, None)
    Field ip6_list


    ipv6_addr (optional, any, None)
      Configure an IPv6 subnet


    uuid (optional, any, None)
      uuid of the object


    others (optional, any, None)
      Disable logging for other L4 protocols


    tcp_list (optional, any, None)
      Field tcp_list


    user_tag (optional, any, None)
      Customized tag


    icmp (optional, any, None)
      Disable logging for icmp traffic


    udp_list (optional, any, None)
      Field udp_list



  ansible_username (True, any, None)
    Username for AXAPI authentication


  tcp_list (False, any, None)
    Field tcp_list


    tcp_port_start (optional, any, None)
      Destination Port (Single Destination Port or Port Range Start)


    tcp_port_end (optional, any, None)
      Port Range End



  ansible_password (True, any, None)
    Password for AXAPI authentication


  udp_list (False, any, None)
    Field udp_list


    udp_port_start (optional, any, None)
      Destination Port (Single Destination Port or Port Range Start)


    udp_port_end (optional, any, None)
      Port Range End



  logging_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  others (False, any, None)
    Disable logging for other L4 protocols


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  icmp (False, any, None)
    Disable logging for icmp traffic


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ip_list (False, any, None)
    Field ip_list


    ipv4_addr (optional, any, None)
      Configure an IP subnet


    uuid (optional, any, None)
      uuid of the object


    others (optional, any, None)
      Disable logging for other L4 protocols


    tcp_list (optional, any, None)
      Field tcp_list


    user_tag (optional, any, None)
      Customized tag


    icmp (optional, any, None)
      Disable logging for icmp traffic


    udp_list (optional, any, None)
      Field udp_list










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


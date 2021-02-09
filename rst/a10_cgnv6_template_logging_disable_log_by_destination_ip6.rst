.. _a10_cgnv6_template_logging_disable_log_by_destination_ip6_module:


a10_cgnv6_template_logging_disable_log_by_destination_ip6 -- Configures A10 cgnv6.template.logging.disable.log.by.destination.ip6
=================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure a filter IPv6 enrty






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


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



  ipv6_addr (True, any, None)
    Configure an IPv6 subnet


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


  user_tag (False, any, None)
    Customized tag









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


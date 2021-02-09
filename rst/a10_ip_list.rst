.. _a10_ip_list_module:


a10_ip_list -- Configures A10 ip-list
=====================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure ip list






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Specify name of the ip list


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ipv6_prefix_config (False, any, None)
    Field ipv6_prefix_config


    count (optional, any, None)
      Number of IPv6 prefixes


    ipv6_addr_prefix (optional, any, None)
      IPv6 Prefix Range Start / IPv6 Prefix


    ipv6_prefix_to (optional, any, None)
      IPv6 Prefix Range End



  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ipv6_config (False, any, None)
    Field ipv6_config


    ipv6_end_addr (optional, any, None)
      IPv6 Range End Address


    ipv6_start_addr (optional, any, None)
      IPv6 Range Start Address / IPv6 Address



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ipv4_config (False, any, None)
    Field ipv4_config


    ipv4_start_addr (optional, any, None)
      IPv4 Range Start Address / IPv4 Address


    ipv4_end_addr (optional, any, None)
      IPv4 Range End Address



  uuid (False, any, None)
    uuid of the object









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


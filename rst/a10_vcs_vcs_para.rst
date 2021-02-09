.. _a10_vcs_vcs_para_module:


a10_vcs_vcs_para -- Configures A10 vcs.vcs-para
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Virtual Chassis System Paramter






Parameters
----------

  time_interval (False, any, None)
    how long between heartbeats (in unit of second, default is 3)


  floating_ip_cfg (False, any, None)
    Field floating_ip_cfg


    floating_ip_mask (optional, any, None)
      Netmask


    floating_ip (optional, any, None)
      Floating IP address (IPv4 address)



  ansible_username (True, any, None)
    Username for AXAPI authentication


  forever (False, any, None)
    VCS retry forever if fails to join the chassis


  multicast_ip (False, any, None)
    Multicast (group) IP address (Multicast IP address)


  dead_interval (False, any, None)
    The node will be considered dead as lack of hearbeats after this time (in unit of second, 10 by default)


  ssl_enable (False, any, None)
    Enable SSL


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  multicast_port (False, any, None)
    Port used in multicast communication (Port number)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  size (False, any, None)
    file size (MBytes) to transmit to monitor the TCP channel


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  multicast_ipv6 (False, any, None)
    Multicast (group) IPv6 address (Multicast IPv6 address)


  failure_retry_count_value (False, any, None)
    0-255, default is 2


  speed_limit (False, any, None)
    speed (KByte/s) limitation for the transmit monitor


  state (True, any, None)
    State of the object to be created.


  floating_ipv6_cfg (False, any, None)
    Field floating_ipv6_cfg


    floating_ipv6 (optional, any, None)
      Floating IPv6 address



  config_seq (False, any, None)
    Configuration sequence number


  ansible_password (True, any, None)
    Password for AXAPI authentication


  force_wait_interval (False, any, None)
    The node will wait the specified time interval before it start aVCS (in unit of second (default is 5))









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


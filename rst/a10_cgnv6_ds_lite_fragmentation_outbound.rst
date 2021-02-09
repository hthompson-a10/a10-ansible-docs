.. _a10_cgnv6_ds_lite_fragmentation_outbound_module:


a10_cgnv6_ds_lite_fragmentation_outbound -- Configures A10 cgnv6.ds.lite.fragmentation.outbound
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DS-Lite Outbound Fragmentation Rules (default= ipv4)






Parameters
----------

  count (False, any, None)
    Configure number of ICMP messages sent when DF set. Default is 1


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  df_set (False, any, None)
    'drop'= Drop Silently; 'ipv4'= Use IPv4 Fragmentation; 'send-icmp'= Send ICMP Type 3 Code 4 (Fragmentation Needed and DF Set) (default); 'send-icmpv6'= Send ICMP Type 2 Code 0 (Packet Too Big);


  state (True, any, None)
    State of the object to be created.


  frag_action (False, any, None)
    'drop'= Drop Silently; 'ipv4'= Use IPv4 fragmentation for oversize packets (default); 'send-icmpv6'= Send ICMPv6 Type 2 Code 0 (Packet Too Big);


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication









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


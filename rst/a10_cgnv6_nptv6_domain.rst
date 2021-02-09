.. _a10_cgnv6_nptv6_domain_module:


a10_cgnv6_nptv6_domain -- Configures A10 cgnv6.nptv6.domain
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure NPTv6 translation domain






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'outbound-packets'= Outbound Packets; 'inbound-packets'= Inbound Packets; 'hairpin-packets'= Hairpin Packets; 'address-not-valid-for- translation'= Address Not Valid For Translation; 'inbound-packets-no-map'= Inbound Packets No Map; 'packets-dest-unreachable'= Packets Destination Unreachable;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    inbound_packets (optional, any, None)
      Inbound Packets


    packets_dest_unreachable (optional, any, None)
      Packets Destination Unreachable


    hairpin_packets (optional, any, None)
      Hairpin Packets


    inbound_packets_no_map (optional, any, None)
      Inbound Packets No Map


    address_not_valid_for_translation (optional, any, None)
      Address Not Valid For Translation


    outbound_packets (optional, any, None)
      Outbound Packets


    name (optional, any, None)
      Name of NPTv6 domain



  name (True, any, None)
    Name of NPTv6 domain


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  outside_prefix (False, any, None)
    Configure outside network prefix (Outside IPv6 network prefix)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  inside_prefix (False, any, None)
    Configure inside network prefix (Inside IPv6 network prefix)


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


.. _a10_system_ndisc_ra_module:


a10_system_ndisc_ra -- Configures A10 system.ndisc-ra
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Neighbor discovery and RA counters






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'good_recv'= Good Router Solicitations (R.S.) Received; 'periodic_sent'= Periodic Router Advertisements (R.A.) Sent; 'rate_limit'= R.S. Rate Limited; 'bad_hop_limit'= R.S. Bad Hop Limit; 'truncated'= R.S. Truncated; 'bad_icmpv6_csum'= R.S. Bad ICMPv6 Checksum; 'bad_icmpv6_code'= R.S. Unknown ICMPv6 Code; 'bad_icmpv6_option'= R.S. Bad ICMPv6 Option; 'l2_addr_and_unspec'= R.S. Src Link-Layer Option and Unspecified Address; 'no_free_buffers'= No Free Buffers to send R.A.;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    bad_hop_limit (optional, any, None)
      R.S. Bad Hop Limit


    bad_icmpv6_code (optional, any, None)
      R.S. Unknown ICMPv6 Code


    bad_icmpv6_csum (optional, any, None)
      R.S. Bad ICMPv6 Checksum


    truncated (optional, any, None)
      R.S. Truncated


    rate_limit (optional, any, None)
      R.S. Rate Limited


    l2_addr_and_unspec (optional, any, None)
      R.S. Src Link-Layer Option and Unspecified Address


    bad_icmpv6_option (optional, any, None)
      R.S. Bad ICMPv6 Option


    periodic_sent (optional, any, None)
      Periodic Router Advertisements (R.A.) Sent


    good_recv (optional, any, None)
      Good Router Solicitations (R.S.) Received


    no_free_buffers (optional, any, None)
      No Free Buffers to send R.A.



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


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


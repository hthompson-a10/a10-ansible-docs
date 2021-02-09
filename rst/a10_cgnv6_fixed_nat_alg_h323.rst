.. _a10_cgnv6_fixed_nat_alg_h323_module:


a10_cgnv6_fixed_nat_alg_h323 -- Configures A10 cgnv6.fixed.nat.alg.h323
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change Fixed NAT H323 ALG Settings






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'h225ras-message'= H323 H225 RAS Message; 'h225cs-message'= H323 H225 Call Signaling Message; 'h245ctl-message'= H323 H245 Media Control Message; 'h245-tunneled'= H323 H245 Tunnelled Message; 'fast-start'= H323 FastStart; 'parse-error'= Message Parse Error; 'message-cross-multi-packets'= H323 Message Cross Multiple Packets; 'conn-ext-creation-failure'= H323 Packet Rewrite Failure; 'rewrite-failure'= H323 Message Rewrite Failure; 'tcp-out-of- order-drop'= TCP Out-of-Order Drop; 'h245-dynamic-addr-exceed'= H323 H245 Dynamic Address Exceed;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    h245ctl_message (optional, any, None)
      H323 H245 Media Control Message


    h245_tunneled (optional, any, None)
      H323 H245 Tunnelled Message


    fast_start (optional, any, None)
      H323 FastStart


    h225ras_message (optional, any, None)
      H323 H225 RAS Message


    h225cs_message (optional, any, None)
      H323 H225 Call Signaling Message



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


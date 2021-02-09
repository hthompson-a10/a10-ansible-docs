.. _a10_network_twamp_responder_ipv6_module:


a10_network_twamp_responder_ipv6 -- Configures A10 network.twamp.responder.ipv6
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure TWAMP responder






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    other_err_v6 (optional, any, None)
      IPv6 Other error drop


    rx_drop_not_enabled_v6 (optional, any, None)
      Rx IPv6 disabled drop


    no_route_err_v6 (optional, any, None)
      Tx IPv6 no route error drop


    rx_pkts_v6 (optional, any, None)
      Rx IPv6 TWAMP test packets


    twamp_hdr_len_err_v6 (optional, any, None)
      Rx IPv6 TWAMP hdr length error drop


    tx_pkts_v6 (optional, any, None)
      Tx IPv6 TWAMP test packets


    rx_acl_drop_v6 (optional, any, None)
      Rx IPv6 client-list drop



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  v6_acl_name (False, any, None)
    Apply an access list (Named Access List)


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


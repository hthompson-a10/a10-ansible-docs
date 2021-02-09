.. _a10_network_twamp_responder_ip_module:


a10_network_twamp_responder_ip -- Configures A10 network.twamp.responder.ip
===========================================================================

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


    rx_drop_not_enabled_v4 (optional, any, None)
      Rx IP disabled drop


    rx_pkts (optional, any, None)
      Rx IP TWAMP test packets


    other_err (optional, any, None)
      IP other error drop


    tx_pkts (optional, any, None)
      Tx IP TWAMP test packets


    twamp_hdr_len_err (optional, any, None)
      Rx TWAMP hdr length error drop


    rx_acl_drop (optional, any, None)
      Rx IP client-list drop


    no_route_err (optional, any, None)
      Tx IP no route error drop



  uuid (False, any, None)
    uuid of the object


  acl_name (False, any, None)
    Apply a named access list (Access List name)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  acl_id (False, any, None)
    ACL id


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


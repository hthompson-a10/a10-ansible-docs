.. _a10_debug_bgp_module:


a10_debug_bgp -- Configures A10 debug.bgp
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Debug Border Gateway Protocol (BGP)






Parameters
----------

  all (False, any, None)
    all debugging


  nin (False, any, None)
    Inbound updates


  nsm (False, any, None)
    NSM message


  ansible_username (True, any, None)
    Username for AXAPI authentication


  nht (False, any, None)
    NHT message


  updates (False, any, None)
    BGP updates


  filters (False, any, None)
    BGP filters


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  out (False, any, None)
    Outbound updates


  ansible_port (True, any, None)
    Port for AXAPI authentication


  dampening (False, any, None)
    BGP Dampening


  uuid (False, any, None)
    uuid of the object


  bfd (False, any, None)
    Bidirectional Forwarding Detection (BFD)


  fsm (False, any, None)
    BGP Finite State Machine


  state (True, any, None)
    State of the object to be created.


  keepalives (False, any, None)
    BGP keepalives


  ansible_password (True, any, None)
    Password for AXAPI authentication


  events (False, any, None)
    BGP events









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


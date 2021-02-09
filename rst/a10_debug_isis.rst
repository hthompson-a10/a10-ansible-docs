.. _a10_debug_isis_module:


a10_debug_isis -- Configures A10 debug.isis
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Intermediate System - Intermediate System (IS-IS)






Parameters
----------

  all (False, any, None)
    Enable all debugging


  ifsm (False, any, None)
    IS-IS Interface Finite State Machine


  ansible_username (True, any, None)
    Username for AXAPI authentication


  nfsm (False, any, None)
    IS-IS Neighbor Finite State Machine


  lsp (False, any, None)
    IS-IS Link State PDU


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  spf (False, any, None)
    IS-IS SPF Calculation


  nsm (False, any, None)
    IS-IS NSM information


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  bfd (False, any, None)
    Bidirectional Forwarding Detection (BFD)


  pdu (False, any, None)
    IS-IS Protocol Data Unit


  state (True, any, None)
    State of the object to be created.


  ansible_password (True, any, None)
    Password for AXAPI authentication


  events (False, any, None)
    IS-IS Events









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


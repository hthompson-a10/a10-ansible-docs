.. _a10_debug_ipv6_ospf_packet_module:


a10_debug_ipv6_ospf_packet -- Configures A10 debug.ipv6.ospf.packet
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

OSPFv3 packets






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  dd (False, any, None)
    OSPFv3 Database Description


  ls_request (False, any, None)
    OSPFv3 Link State Request


  ls_update (False, any, None)
    OSPFv3 Link State Update


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  recv (False, any, None)
    Packet received


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ls_ack (False, any, None)
    OSPFv3 Link State Acknowledgment


  detail (False, any, None)
    Detail information


  send (False, any, None)
    Packet sent


  state (True, any, None)
    State of the object to be created.


  ansible_password (True, any, None)
    Password for AXAPI authentication


  hello (False, any, None)
    OSPFv3 Hello









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


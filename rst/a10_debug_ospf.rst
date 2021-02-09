.. _a10_debug_ospf_module:


a10_debug_ospf -- Configures A10 debug.ospf
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Debug Open Shortest Path First (OSPF)






Parameters
----------

  all (False, any, None)
    Field all


    uuid (optional, any, None)
      uuid of the object



  ifsm (False, any, None)
    Field ifsm


    status (optional, any, None)
      IFSM Status Information


    timers (optional, any, None)
      IFSM Timer Information


    events (optional, any, None)
      IFSM Event Information


    uuid (optional, any, None)
      uuid of the object



  ansible_username (True, any, None)
    Username for AXAPI authentication


  nfsm (False, any, None)
    Field nfsm


    status (optional, any, None)
      NFSM Status Information


    timers (optional, any, None)
      NFSM Timer Information


    events (optional, any, None)
      NFSM Event Information


    uuid (optional, any, None)
      uuid of the object



  packet (False, any, None)
    Field packet


    uuid (optional, any, None)
      uuid of the object


    ls_ack (optional, any, None)
      OSPFv3 Link State Acknowledgment


    dd (optional, any, None)
      OSPFv3 Database Description


    ls_request (optional, any, None)
      OSPFv3 Link State Request


    detail (optional, any, None)
      Detail information


    send (optional, any, None)
      Packet sent


    ls_update (optional, any, None)
      OSPFv3 Link State Update


    recv (optional, any, None)
      Packet received


    hello (optional, any, None)
      OSPFv3 Hello



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  nsm (False, any, None)
    Field nsm


    interface (optional, any, None)
      NSM interface


    redistribute (optional, any, None)
      NSM redistribute


    uuid (optional, any, None)
      uuid of the object



  ansible_port (True, any, None)
    Port for AXAPI authentication


  bfd (False, any, None)
    Field bfd


    uuid (optional, any, None)
      uuid of the object



  route (False, any, None)
    Field route


    ia (optional, any, None)
      Inter-Area route calculation information


    ase (optional, any, None)
      External route calculation information


    install (optional, any, None)
      Route installation information


    spf (optional, any, None)
      SPF calculation information


    uuid (optional, any, None)
      uuid of the object



  lsa (False, any, None)
    Field lsa


    gererate (optional, any, None)
      LSA Generation


    uuid (optional, any, None)
      uuid of the object


    install (optional, any, None)
      LSA Installation


    flooding (optional, any, None)
      LSA Flooding


    maxage (optional, any, None)
      LSA MaxAge processing


    refresh (optional, any, None)
      LSA Refreshment



  state (True, any, None)
    State of the object to be created.


  ansible_password (True, any, None)
    Password for AXAPI authentication


  events (False, any, None)
    Field events


    asbr (optional, any, None)
      OSPF ASBR events


    abr (optional, any, None)
      OSPF ABR events


    uuid (optional, any, None)
      uuid of the object


    router (optional, any, None)
      Other router events


    vlink (optional, any, None)
      Virtual-Link event


    os (optional, any, None)
      OS events










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


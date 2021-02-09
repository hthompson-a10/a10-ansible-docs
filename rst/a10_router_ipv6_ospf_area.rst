.. _a10_router_ipv6_ospf_area_module:


a10_router_ipv6_ospf_area -- Configures A10 router.ipv6.ospf.area
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

OSPF area parameters






Parameters
----------

  range_list (False, any, None)
    Field range_list


    option (optional, any, None)
      'advertise'= Advertise this range (default); 'not-advertise'= DoNotAdvertise this range;


    value (optional, any, None)
      Area range for IPv6 prefix



  ansible_username (True, any, None)
    Username for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  area_num (True, any, None)
    OSPFv3 area ID as a decimal value


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ospf_process_id (optional, any, None)
    Key to identify parent object


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  virtual_link_list (False, any, None)
    Field virtual_link_list


    instance_id (optional, any, None)
      OSPFv3 instance ID


    retransmit_interval (optional, any, None)
      LSA retransmit interval (Seconds)


    dead_interval (optional, any, None)
      Dead router detection time (Seconds)


    transmit_delay (optional, any, None)
      LSA transmission delay (Seconds)


    hello_interval (optional, any, None)
      Hello packet interval (Seconds)


    bfd (optional, any, None)
      Bidirectional Forwarding Detection (BFD)


    value (optional, any, None)
      ID (IP addr) associated with virtual link neighbor



  area_ipv4 (True, any, None)
    OSPFv3 area ID in IP address format


  stub (False, any, None)
    Configure OSPFv3 area as stub


  default_cost (False, any, None)
    Set the summary-default cost of a NSSA or stub area (Stub's advertised default summary cost)


  no_summary (False, any, None)
    Do not inject inter-area routes into area


  ansible_password (True, any, None)
    Password for AXAPI authentication









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


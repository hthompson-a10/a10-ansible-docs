.. _a10_interface_trunk_ipv6_ospf_module:


a10_interface_trunk_ipv6_ospf -- Configures A10 interface.trunk.ipv6.ospf
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Open Shortest Path First for IPv6 (OSPFv3)






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  hello_interval_cfg (False, any, None)
    Field hello_interval_cfg


    instance_id (optional, any, None)
      Specify the interface instance ID


    hello_interval (optional, any, None)
      Time between HELLO packets (Seconds)



  cost_cfg (False, any, None)
    Field cost_cfg


    instance_id (optional, any, None)
      Specify the interface instance ID


    cost (optional, any, None)
      Interface cost



  neighbor_cfg (False, any, None)
    Field neighbor_cfg


    neighbor_poll_interval (optional, any, None)
      OSPF dead-router polling interval (Seconds)


    neig_inst (optional, any, None)
      Specify the interface instance ID


    neighbor_priority (optional, any, None)
      OSPF priority of non-broadcast neighbor


    neighbor (optional, any, None)
      OSPFv3 neighbor (Neighbor IPv6 address)


    neighbor_cost (optional, any, None)
      OSPF cost for point-to-multipoint neighbor (metric)



  dead_interval_cfg (False, any, None)
    Field dead_interval_cfg


    instance_id (optional, any, None)
      Specify the interface instance ID


    dead_interval (optional, any, None)
      Interval after which a neighbor is declared dead (Seconds)



  disable (False, any, None)
    Disable BFD


  mtu_ignore_cfg (False, any, None)
    Field mtu_ignore_cfg


    instance_id (optional, any, None)
      Specify the interface instance ID


    mtu_ignore (optional, any, None)
      Ignores the MTU in DBD packets



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  bfd (False, any, None)
    Bidirectional Forwarding Detection (BFD)


  retransmit_interval_cfg (False, any, None)
    Field retransmit_interval_cfg


    instance_id (optional, any, None)
      Specify the interface instance ID


    retransmit_interval (optional, any, None)
      Time between retransmitting lost link state advertisements (Seconds)



  trunk_ifnum (optional, any, None)
    Key to identify parent object


  network_list (False, any, None)
    Field network_list


    p2mp_nbma (optional, any, None)
      Specify non-broadcast point-to-multipoint network


    broadcast_type (optional, any, None)
      'broadcast'= Specify OSPF broadcast multi-access network; 'non-broadcast'= Specify OSPF NBMA network; 'point-to-point'= Specify OSPF point-to-point network; 'point-to-multipoint'= Specify OSPF point-to-multipoint network;


    network_instance_id (optional, any, None)
      Specify the interface instance ID



  transmit_delay_cfg (False, any, None)
    Field transmit_delay_cfg


    instance_id (optional, any, None)
      Specify the interface instance ID


    transmit_delay (optional, any, None)
      Link state transmit delay (Seconds)



  state (True, any, None)
    State of the object to be created.


  priority_cfg (False, any, None)
    Field priority_cfg


    priority (optional, any, None)
      Router priority


    instance_id (optional, any, None)
      Specify the interface instance ID



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


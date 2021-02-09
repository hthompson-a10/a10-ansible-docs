.. _a10_network_vlan_module:


a10_network_vlan -- Configures A10 network.vlan
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure VLAN






Parameters
----------

  oper (False, any, None)
    Field oper


    tagg_eth_ports (optional, any, None)
      Field tagg_eth_ports


    vlan_name (optional, any, None)
      Field vlan_name


    un_tagg_logical_ports (optional, any, None)
      Field un_tagg_logical_ports


    vlan_num (optional, any, None)
      VLAN number


    tagg_logical_ports (optional, any, None)
      Field tagg_logical_ports


    ve_num (optional, any, None)
      Field ve_num


    is_shared_vlan (optional, any, None)
      Field is_shared_vlan


    un_tagg_eth_ports (optional, any, None)
      Field un_tagg_eth_ports



  tagged_trunk_list (False, any, None)
    Field tagged_trunk_list


    tagged_trunk_start (optional, any, None)
      Trunk groups


    tagged_trunk_end (optional, any, None)
      Trunk Group



  ve (False, any, None)
    ve number


  ansible_username (True, any, None)
    Username for AXAPI authentication


  untagged_trunk_list (False, any, None)
    Field untagged_trunk_list


    untagged_trunk_start (optional, any, None)
      Trunk groups


    untagged_trunk_end (optional, any, None)
      Trunk Group



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  tagged_eth_list (False, any, None)
    Field tagged_eth_list


    tagged_ethernet_start (optional, any, None)
      Ethernet port (Interface number)


    tagged_ethernet_end (optional, any, None)
      Ethernet port



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (False, any, None)
    VLAN name


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'broadcast_count'= Broadcast counter; 'multicast_count'= Multicast counter; 'ip_multicast_count'= IP Multicast counter; 'unknown_unicast_count'= Unknown Unicast counter; 'mac_movement_count'= Mac Movement counter; 'shared_vlan_partition_switched_counter'= SVLAN Partition switched counter;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    mac_movement_count (optional, any, None)
      Mac Movement counter


    vlan_num (optional, any, None)
      VLAN number


    multicast_count (optional, any, None)
      Multicast counter


    shared_vlan_partition_switched_counter (optional, any, None)
      SVLAN Partition switched counter


    ip_multicast_count (optional, any, None)
      IP Multicast counter


    unknown_unicast_count (optional, any, None)
      Unknown Unicast counter


    broadcast_count (optional, any, None)
      Broadcast counter



  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  vlan_num (True, any, None)
    VLAN number


  untagged_eth_list (False, any, None)
    Field untagged_eth_list


    untagged_ethernet_end (optional, any, None)
      Ethernet port


    untagged_ethernet_start (optional, any, None)
      Ethernet port (Interface number)



  state (True, any, None)
    State of the object to be created.


  untagged_lif (False, any, None)
    Logical tunnel interface (Logical tunnel interface number)


  shared_vlan (False, any, None)
    Configure VLAN as a shared VLAN


  user_tag (False, any, None)
    Customized tag


  traffic_distribution_mode (False, any, None)
    'sip'= sip; 'dip'= dip; 'primary'= primary; 'blade'= blade; 'l4-src-port'= l4-src-port; 'l4-dst-port'= l4-dst-port;









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


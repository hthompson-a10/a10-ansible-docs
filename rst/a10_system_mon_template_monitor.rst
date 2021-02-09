.. _a10_system_mon_template_monitor_module:


a10_system_mon_template_monitor -- Configures A10 system.mon.template.monitor
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Monitor template






Parameters
----------

  link_down_cfg (False, any, None)
    Field link_down_cfg


    linkdown_ethernet1 (optional, any, None)
      Specify the port physical port number (Ethernet interface number)


    linkdown_ethernet2 (optional, any, None)
      Specify the port physical port number (Ethernet interface number)


    linkdown_ethernet3 (optional, any, None)
      Specify the port physical port number (Ethernet interface number)


    link_down_sequence1 (optional, any, None)
      Sequence number (Specify the sequence number)


    link_down_sequence2 (optional, any, None)
      Sequence number (Specify the seqeuence number)


    link_down_sequence3 (optional, any, None)
      Sequence number (Specify the sequence number)



  link_disable_cfg (False, any, None)
    Field link_disable_cfg


    dis_sequence (optional, any, None)
      Sequence number (Specify the sequence number)


    diseth (optional, any, None)
      Specify the physical port number (Ethernet interface number)



  ansible_username (True, any, None)
    Username for AXAPI authentication


  link_up_cfg (False, any, None)
    Field link_up_cfg


    linkup_ethernet1 (optional, any, None)
      Specify the port physical port number (Ethernet interface number)


    linkup_ethernet3 (optional, any, None)
      Specify the port physical port number (Ethernet interface number)


    linkup_ethernet2 (optional, any, None)
      Specify the port physical port number (Ethernet interface number)


    link_up_sequence1 (optional, any, None)
      Sequence number (Specify the sequence number)


    link_up_sequence3 (optional, any, None)
      Sequence number (Specify the sequece number)


    link_up_sequence2 (optional, any, None)
      Sequence number (Specify the sequence number)



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  id (True, any, None)
    Monitor template ID Number


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  clear_cfg (False, any, None)
    Field clear_cfg


    sessions (optional, any, None)
      'all'= Clear all sessions; 'sequence'= Sequence number;


    clear_sequence (optional, any, None)
      Specify the port physical port number


    clear_all_sequence (optional, any, None)
      Sequence number (Specify the port physical port number)



  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


  ansible_host (True, any, None)
    Host for AXAPI authentication


  monitor_relation (False, any, None)
    'monitor-and'= Configures the monitors in current template to work with AND logic; 'monitor-or'= Configures the monitors in current template to work with OR logic;


  link_enable_cfg (False, any, None)
    Field link_enable_cfg


    enaeth (optional, any, None)
      Specify the physical port number (Ethernet interface number)


    ena_sequence (optional, any, None)
      Sequence number (Specify the sequence number)



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


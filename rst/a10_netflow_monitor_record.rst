.. _a10_netflow_monitor_record_module:


a10_netflow_monitor_record -- Configures A10 netflow.monitor.record
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure record types to be exported






Parameters
----------

  port_batch_v2_dslite (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  nat64 (False, any, None)
    NAT64 Flow Record Template


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  sesn_event_nat44 (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  port_batch_nat44 (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  monitor_name (optional, any, None)
    Key to identify parent object


  ansible_host (True, any, None)
    Host for AXAPI authentication


  port_mapping_dslite (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  sesn_event_nat64 (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  nat44 (False, any, None)
    NAT44 Flow Record Template


  ansible_port (True, any, None)
    Port for AXAPI authentication


  port_batch_v2_nat44 (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  uuid (False, any, None)
    uuid of the object


  port_batch_nat64 (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  sesn_event_fw6 (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  sesn_event_fw4 (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  sesn_event_dslite (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  dslite (False, any, None)
    DS-Lite Flow Record Template


  port_batch_v2_nat64 (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  port_mapping_nat44 (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  port_batch_dslite (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  state (True, any, None)
    State of the object to be created.


  netflow_v5 (False, any, None)
    NetFlow V5 Flow Record Template


  port_mapping_nat64 (False, any, None)
    'both'= Export both creation and deletion events; 'creation'= Export only creation events; 'deletion'= Export only deletion events;


  netflow_v5_ext (False, any, None)
    Extended NetFlow V5 Flow Record Template, supports ipv6


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


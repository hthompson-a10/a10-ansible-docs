.. _a10_netflow_monitor_custom_record_module:


a10_netflow_monitor_custom_record -- Configures A10 netflow.monitor.custom-record
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure custom record types to be exported






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


  custom_cfg (False, any, None)
    Field custom_cfg


    ipfix_template (optional, any, None)
      Custom IPFIX Template


    event (optional, any, None)
      'sesn-event-nat44-creation'= Export NAT44 session creation events; 'sesn-event- nat44-deletion'= Export NAT44 session deletion events; 'sesn-event- nat64-creation'= Export NAT64 session creation events; 'sesn-event- nat64-deletion'= Export NAT64 session deletion events; 'sesn-event-dslite- creation'= Export Dslite session creation events; 'sesn-event-dslite-deletion'= Export Dslite session deletion events; 'sesn-event-fw4-creation'= Export FW4 session creation events; 'sesn-event-fw4-deletion'= Export FW4 session deletion events; 'sesn-event-fw6-creation'= Export FW6 session creation events; 'sesn- event-fw6-deletion'= Export FW6 session deletion events; 'deny-reset-event- fw4'= Export FW4 Deny Reset events; 'deny-reset-event-fw6'= Export FW6 Deny Reset events; 'port-mapping-nat44-creation'= Export NAT44 Port Mapping Creation Event; 'port-mapping-nat44-deletion'= Export NAT44 Port Mapping Deletion Event; 'port-mapping-nat64-creation'= Export NAT64 Port Mapping Creation Event; 'port- mapping-nat64-deletion'= Export NAT64 Port Mapping Deletion Event; 'port- mapping-dslite-creation'= Export Dslite Port Mapping Creation Event; 'port- mapping-dslite-deletion'= Export Dslite Port Mapping Deletion Event; 'port- batch-nat44-creation'= Export NAT44 Port Batch Creation Event; 'port-batch- nat44-deletion'= Export NAT44 Port Batch Deletion Event; 'port-batch- nat64-creation'= Export NAT64 Port Batch Creation Event; 'port-batch- nat64-deletion'= Export NAT64 Port Batch Deletion Event; 'port-batch-dslite- creation'= Export Dslite Port Batch Creation Event; 'port-batch-dslite- deletion'= Export Dslite Port Batch Deletion Event; 'port- batch-v2-nat44-creation'= Export NAT44 Port Batch v2 Creation Event; 'port- batch-v2-nat44-deletion'= Export NAT44 Port Batch v2 Deletion Event; 'port- batch-v2-nat64-creation'= Export NAT64 Port Batch v2 Creation Event; 'port- batch-v2-nat64-deletion'= Export NAT64 Port Batch v2 Deletion Event; 'port- batch-v2-dslite-creation'= Export Dslite Port Batch v2 Creation Event; 'port- batch-v2-dslite-deletion'= Export Dslite Port Batch v2 Deletion Event;



  ansible_password (True, any, None)
    Password for AXAPI authentication


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


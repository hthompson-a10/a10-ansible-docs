.. _a10_visibility_flow_collector_netflow_template_module:


a10_visibility_flow_collector_netflow_template -- Configures A10 visibility.flow.collector.netflow.template
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

NetFlow/IPFIX collector templates






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'templates-added-to-delq'= Netflow templates added to the delete queue; 'templates-removed-from-delq'= Netflow templates removed from the delete queue;



  oper (False, any, None)
    Field oper


    nf_template_list (optional, any, None)
      Field nf_template_list


    detail (optional, any, None)
      Field detail



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    templates_added_to_delq (optional, any, None)
      Netflow templates added to the delete queue


    templates_removed_from_delq (optional, any, None)
      Netflow templates removed from the delete queue



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  detail (False, any, None)
    Field detail


    uuid (optional, any, None)
      uuid of the object



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


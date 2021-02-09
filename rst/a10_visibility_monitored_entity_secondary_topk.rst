.. _a10_visibility_monitored_entity_secondary_topk_module:


a10_visibility_monitored_entity_secondary_topk -- Configures A10 visibility.monitored.entity.secondary.topk
===========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Display topk secondary Monitoring entities






Parameters
----------

  oper (False, any, None)
    Field oper


    sources (optional, any, None)
      Field sources


    ipv6_addr (optional, any, None)
      Field ipv6_addr


    ipv4_addr (optional, any, None)
      Field ipv4_addr


    l4_proto (optional, any, None)
      Field l4_proto


    metric_topk_list (optional, any, None)
      Field metric_topk_list


    l4_port (optional, any, None)
      Field l4_port



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  sources (False, any, None)
    Field sources


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


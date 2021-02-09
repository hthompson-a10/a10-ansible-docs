.. _a10_slb_template_policy_forward_policy_source_destination_class_list_module:


a10_slb_template_policy_forward_policy_source_destination_class_list -- Configures A10 slb.template.policy.forward.policy.source.destination.class-list
=======================================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure class-list for destination matching






Parameters
----------

  dest_class_list (True, any, None)
    Destination Class List Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ntype (False, any, None)
    'host'= Match hostname; 'url'= Match URL; 'ip'= Match destination IP address;


  policy_name (optional, any, None)
    Key to identify parent object


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'hits'= Number of requests matching this destination rule;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    hits (optional, any, None)
      Number of requests matching this destination rule


    dest_class_list (optional, any, None)
      Destination Class List Name



  name (optional, any, None)
    Key to identify parent object


  priority (False, any, None)
    Priority value of the action(higher the number higher the priority)


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    Action to be performed


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


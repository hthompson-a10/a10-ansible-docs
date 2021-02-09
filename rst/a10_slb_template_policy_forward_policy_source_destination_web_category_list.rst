.. _a10_slb_template_policy_forward_policy_source_destination_web_category_list_module:


a10_slb_template_policy_forward_policy_source_destination_web_category_list -- Configures A10 slb.template.policy.forward.policy.source.destination.web-category-list
=====================================================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure web-category category-list for destination matching






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  web_category_list (True, any, None)
    Destination Web Category List Name


  ntype (False, any, None)
    'host'= Match hostname; 'url'= match URL;


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


    web_category_list (optional, any, None)
      Destination Web Category List Name


    hits (optional, any, None)
      Number of requests matching this destination rule



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


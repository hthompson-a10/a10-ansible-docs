.. _a10_slb_template_policy_forward_policy_source_module:


a10_slb_template_policy_forward_policy_source -- Configures A10 slb.template.policy.forward.policy.source
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

proxy source list






Parameters
----------

  match_authorize_policy (False, any, None)
    Authorize-policy for user and group based policy


  ansible_username (True, any, None)
    Username for AXAPI authentication


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
      'all'= all; 'hits'= Number of requests matching this source rule; 'destination- match-not-found'= Number of requests without matching destination rule; 'no- host-info'= Failed to parse ip or host information from request;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    hits (optional, any, None)
      Number of requests matching this source rule


    destination (optional, any, None)
      Field destination


    no_host_info (optional, any, None)
      Failed to parse ip or host information from request


    destination_match_not_found (optional, any, None)
      Number of requests without matching destination rule


    name (optional, any, None)
      source destination match rule name



  name (True, any, None)
    source destination match rule name


  user_tag (False, any, None)
    Customized tag


  destination (False, any, None)
    Field destination


    web_category_list_list (optional, any, None)
      Field web_category_list_list


    any (optional, any, None)
      Field any


    class_list_list (optional, any, None)
      Field class_list_list



  match_class_list (False, any, None)
    Class List Name


  priority (False, any, None)
    Priority of the source(higher the number higher the priority, default 0)


  state (True, any, None)
    State of the object to be created.


  ansible_password (True, any, None)
    Password for AXAPI authentication


  match_any (False, any, None)
    Match any source









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


.. _a10_rule_set_track_app_rule_list_module:


a10_rule_set_track_app_rule_list -- Configures A10 rule.set.track-app-rule-list
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field track_app_rule_list






Parameters
----------

  oper (False, any, None)
    Field oper


    rule_list (optional, any, None)
      Field rule_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    dummy (optional, any, None)
      Entry for a10countergen



  uuid (False, any, None)
    uuid of the object


  rule_set_name (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


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


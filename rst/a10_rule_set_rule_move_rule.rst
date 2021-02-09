.. _a10_rule_set_rule_move_rule_module:


a10_rule_set_rule_move_rule -- Configures A10 rule.set.rule.move-rule
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Move Rule






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (optional, any, None)
    Key to identify parent object


  rule_set_name (optional, any, None)
    Key to identify parent object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  target_rule (False, any, None)
    Field target_rule


  state (True, any, None)
    State of the object to be created.


  location (False, any, None)
    'top'= top; 'before'= before; 'after'= after; 'bottom'= bottom;


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


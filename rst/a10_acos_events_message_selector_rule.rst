.. _a10_acos_events_message_selector_rule_module:


a10_acos_events_message_selector_rule -- Configures A10 acos-events.message.selector.rule
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure rules to select messages for which logging is enabled/blocked






Parameters
----------

  severity_oper (False, any, None)
    'equal-and-higher'= emergency is highest, debugging lowest; 'equal'= single severity;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  message_id_scope (False, any, None)
    'all'= Log messages at this level and all sub-trees; 'node-only'= Log messages at this node only; 'children-only'= Log messages at all sub-trees only; 'log- field-only'= Log message for this Log Field only;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  index (True, any, None)
    Specify rule index - rules are applied in numeric order


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


  severity_val (False, any, None)
    'emergency'= System unusable log messages (Most Important); 'alert'= Action must be taken immediately; 'critical'= Critical conditions; 'error'= Error conditions; 'warning'= Warning conditions; 'notification'= Normal but significant conditions; 'information'= Informational messages; 'debugging'= Debug level messages (Least Important);


  message_selector_name (optional, any, None)
    Key to identify parent object


  action (False, any, None)
    'send'= log messages selected by this rule will be sent; 'drop'= log messages selected by this rule will be dropped;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  message_id (False, any, None)
    Select a specific message by message-id and optionally severity









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


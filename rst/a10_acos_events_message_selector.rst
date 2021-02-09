.. _a10_acos_events_message_selector_module:


a10_acos_events_message_selector -- Configures A10 acos-events.message-selector
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure message selector to select messages to be logged/blocked






Parameters
----------

  rule_list (False, any, None)
    Field rule_list


    index (optional, any, None)
      Specify rule index - rules are applied in numeric order


    uuid (optional, any, None)
      uuid of the object


    severity_oper (optional, any, None)
      'equal-and-higher'= emergency is highest, debugging lowest; 'equal'= single severity;


    message_id_scope (optional, any, None)
      'all'= Log messages at this level and all sub-trees; 'node-only'= Log messages at this node only; 'children-only'= Log messages at all sub-trees only; 'log- field-only'= Log message for this Log Field only;


    severity_val (optional, any, None)
      'emergency'= System unusable log messages (Most Important); 'alert'= Action must be taken immediately; 'critical'= Critical conditions; 'error'= Error conditions; 'warning'= Warning conditions; 'notification'= Normal but significant conditions; 'information'= Informational messages; 'debugging'= Debug level messages (Least Important);


    action (optional, any, None)
      'send'= log messages selected by this rule will be sent; 'drop'= log messages selected by this rule will be dropped;


    user_tag (optional, any, None)
      Customized tag


    message_id (optional, any, None)
      Select a specific message by message-id and optionally severity



  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Specify message selector name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


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


  uuid (False, any, None)
    uuid of the object









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


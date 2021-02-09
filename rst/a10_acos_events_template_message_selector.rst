.. _a10_acos_events_template_message_selector_module:


a10_acos_events_template_message_selector -- Configures A10 acos-events.template.message-selector
=================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify the message selector






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Specify the message selector name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  collector_group_list (False, any, None)
    Field collector_group_list


    user_tag (optional, any, None)
      Customized tag


    name (optional, any, None)
      Specify the log server group for receiving log messages


    uuid (optional, any, None)
      uuid of the object



  state (True, any, None)
    State of the object to be created.


  template_name (optional, any, None)
    Key to identify parent object


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


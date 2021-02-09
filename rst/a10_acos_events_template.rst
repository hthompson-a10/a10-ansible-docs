.. _a10_acos_events_template_module:


a10_acos_events_template -- Configures A10 acos-events.template
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure logging template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Specify logging template name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  message_selector_list (False, any, None)
    Field message_selector_list


    collector_group_list (optional, any, None)
      Field collector_group_list


    user_tag (optional, any, None)
      Customized tag


    name (optional, any, None)
      Specify the message selector name


    uuid (optional, any, None)
      uuid of the object



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


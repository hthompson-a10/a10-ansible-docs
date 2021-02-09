.. _a10_acos_events_active_template_module:


a10_acos_events_active_template -- Configures A10 acos.events.active-template
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure global logging template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (False, any, None)
    Specify the logging template name


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


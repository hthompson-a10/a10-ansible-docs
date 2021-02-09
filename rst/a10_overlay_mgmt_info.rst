.. _a10_overlay_mgmt_info_module:


a10_overlay_mgmt_info -- Configures A10 overlay-mgmt-info
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Overlay management specific data






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  appstring (True, any, None)
    Application string


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  plugin_name (True, any, None)
    Plugin string


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


.. _a10_merge_mode_add_slb_module:


a10_merge_mode_add_slb -- Configures A10 merge.mode.add.slb
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Control block-merge mode behavior for slb objects






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  virtual_server_port (False, any, None)
    Control block-merge behavior for slb virtual-server port


  member (False, any, None)
    Control block-merge behavior for slb service-group member


  state (True, any, None)
    State of the object to be created.


  server_port (False, any, None)
    Control block-merge behavior for slb server port


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


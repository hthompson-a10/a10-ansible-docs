.. _a10_system_gui_image_list_module:


a10_system_gui_image_list -- Configures A10 system.gui-image-list
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Get Gui Image List






Parameters
----------

  oper (False, any, None)
    Field oper


    pre_pri_gui (optional, any, None)
      Field pre_pri_gui


    pre_sec_gui (optional, any, None)
      Field pre_sec_gui


    gui_list_pri (optional, any, None)
      Field gui_list_pri


    gui_list_sec (optional, any, None)
      Field gui_list_sec



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


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


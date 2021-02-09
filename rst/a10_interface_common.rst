.. _a10_interface_common_module:


a10_interface_common -- Configures A10 interface.common
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Interface statistics information






Parameters
----------

  oper (False, any, None)
    Field oper


    interfaces (optional, any, None)
      Field interfaces


    interval (optional, any, None)
      Field interval


    tot_num_phy_intf (optional, any, None)
      Field tot_num_phy_intf


    vnp_id (optional, any, None)
      Field vnp_id


    time (optional, any, None)
      Field time



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


.. _a10_network_available_trunk_list_module:


a10_network_available_trunk_list -- Configures A10 network.available-trunk-list
===============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

List of ethernet interfaces available in a partition






Parameters
----------

  oper (False, any, None)
    Field oper


    if_list (optional, any, None)
      Field if_list



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


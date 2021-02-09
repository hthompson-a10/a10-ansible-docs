.. _a10_visibility_resource_usage_module:


a10_visibility_resource_usage -- Configures A10 visibility.resource-usage
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Visibility resoruces information






Parameters
----------

  oper (False, any, None)
    Field oper


    resource_list (optional, any, None)
      Field resource_list



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


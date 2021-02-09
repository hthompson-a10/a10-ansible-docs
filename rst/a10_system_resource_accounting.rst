.. _a10_system_resource_accounting_module:


a10_system_resource_accounting -- Configures A10 system.resource-accounting
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create resource accounting template






Parameters
----------

  template_list (False, any, None)
    Field template_list


    system_resources (optional, any, None)
      Field system_resources


    name (optional, any, None)
      Enter template name


    user_tag (optional, any, None)
      Customized tag


    uuid (optional, any, None)
      uuid of the object


    app_resources (optional, any, None)
      Field app_resources


    network_resources (optional, any, None)
      Field network_resources



  oper (False, any, None)
    Field oper


    scope (optional, any, None)
      Field scope


    partition_resource (optional, any, None)
      Field partition_resource



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


.. _a10_authentication_console_module:


a10_authentication_console -- Configures A10 authentication.console
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure console authentication type






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


  state (True, any, None)
    State of the object to be created.


  type_cfg (False, any, None)
    Field type_cfg


    console_type (optional, any, None)
      Field console_type


    ntype (optional, any, None)
      The login authentication type



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


.. _a10_authentication_module:


a10_authentication -- Configures A10 authentication
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure authentication feature






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  console (False, any, None)
    Field console


    type_cfg (optional, any, None)
      Field type_cfg


    uuid (optional, any, None)
      uuid of the object



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  enable_cfg (False, any, None)
    Field enable_cfg


    enable_auth_type (optional, any, None)
      The enable-password authentication type



  state (True, any, None)
    State of the object to be created.


  type_cfg (False, any, None)
    Field type_cfg


    ntype (optional, any, None)
      The login authentication type



  login_cfg (False, any, None)
    Field login_cfg


    privilege_mode (optional, any, None)
      Configure to enter privilege-mode


    local (optional, any, None)
      Configure local user to enter privilege-mode



  mode_cfg (False, any, None)
    Field mode_cfg


    mode (optional, any, None)
      'multiple'= Multiple authentication mode. If an authentication method rejected, try next one; 'single'= Single authentication mode. If an authentication method rejected, don't try next one;



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  multiple_auth_reject (False, any, None)
    Multiple same user login reject


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


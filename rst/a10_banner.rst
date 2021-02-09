.. _a10_banner_module:


a10_banner -- Configures A10 banner
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Define a login banner






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  exec_banner_cfg (False, any, None)
    Field exec_banner_cfg


    nexec (optional, any, None)
      Set EXEC process creation banner


    exec_banner (optional, any, None)
      Banner text, string \n is taken as line break of multi-line banner text, use \\n for \n, \077 for ? and \011 for tab



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  login_banner_cfg (False, any, None)
    Field login_banner_cfg


    login_banner (optional, any, None)
      Banner text, string \n is taken as line break of multi-line banner text, use \\n to indicate \n


    login (optional, any, None)
      Set login banner



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


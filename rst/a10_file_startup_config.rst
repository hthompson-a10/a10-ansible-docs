.. _a10_file_startup_config_module:


a10_file_startup_config -- Configures A10 file.startup-config
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Contents of Startup Configuration






Parameters
----------

  oper (False, any, None)
    Field oper


    current_startup_config (optional, any, None)
      Field current_startup_config


    pri_startup_config (optional, any, None)
      Field pri_startup_config


    sec_startup_config (optional, any, None)
      Field sec_startup_config


    dirty (optional, any, None)
      Field dirty


    file_list (optional, any, None)
      Field file_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  file_handle (False, any, None)
    full path of the uploaded file


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  file_content (False, any, None)
    Content of the uploaded file


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  dst_file (False, any, None)
    destination file name for copy and rename action


  action (False, any, None)
    'import'= import;


  file (False, any, None)
    startup-config local file name


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  size (False, any, None)
    startup-config file size in byte









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


.. _a10_system_geolocation_file_error_info_module:


a10_system_geolocation_file_error_info -- Configures A10 system.geolocation.file.error-info
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Geolocation File Error Information






Parameters
----------

  oper (False, any, None)
    Field oper


    error_list (optional, any, None)
      Field error_list


    filename (optional, any, None)
      Field filename



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


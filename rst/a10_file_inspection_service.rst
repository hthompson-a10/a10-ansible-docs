.. _a10_file_inspection_service_module:


a10_file_inspection_service -- Configures A10 file.inspection.service
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

File Inspection Service related commands






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  enable (False, any, None)
    Enable Internal File Inspection Service


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  file_content (False, any, None)
    Content of the uploaded file


  ansible_password (True, any, None)
    Password for AXAPI authentication


  service_down_action (False, any, None)
    'reset'= Reset Connection; 'allow'= Allow File;


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  health_check_disable (False, any, None)
    Disable internal service health check









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


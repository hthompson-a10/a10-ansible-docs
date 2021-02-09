.. _a10_file_health_external_module:


a10_file_health_external -- Configures A10 file.health-external
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Address the External Script Program






Parameters
----------

  oper (False, any, None)
    Field oper


    file_list (optional, any, None)
      Field file_list



  description (False, any, None)
    Describe the Program Function briefly


  ansible_username (True, any, None)
    Username for AXAPI authentication


  file (False, any, None)
    Specify the Program Name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  size (False, any, None)
    syslog file size in byte


  ansible_port (True, any, None)
    Port for AXAPI authentication


  file_handle (False, any, None)
    full path of the uploaded file


  uuid (False, any, None)
    uuid of the object


  file_content (False, any, None)
    Content of the uploaded file


  state (True, any, None)
    State of the object to be created.


  dst_file (False, any, None)
    destination file name for copy and rename action


  action (False, any, None)
    'create'= create; 'import'= import; 'export'= export; 'copy'= copy; 'rename'= rename; 'check'= check; 'replace'= replace; 'delete'= delete;


  ansible_password (True, any, None)
    Password for AXAPI authentication









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


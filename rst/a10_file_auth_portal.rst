.. _a10_file_auth_portal_module:


a10_file_auth_portal -- Configures A10 file.auth-portal
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Authentication portal file information and management commands






Parameters
----------

  oper (False, any, None)
    Field oper


    file_list (optional, any, None)
      Field file_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  file_handle (False, any, None)
    Full path of the uploaded file


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
    Destination file name for copy and rename action


  action (False, any, None)
    'create'= create; 'import'= import; 'export'= export; 'copy'= copy; 'rename'= rename; 'check'= check; 'replace'= replace; 'delete'= delete;


  file (False, any, None)
    Authentication portal local file name


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  size (False, any, None)
    Authentication portal file size in byte









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


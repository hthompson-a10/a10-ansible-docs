.. _a10_file_aflex_module:


a10_file_aflex -- Configures A10 file.aflex
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

aflex file information and management commands






Parameters
----------

  oper (False, any, None)
    Field oper


    file_list (optional, any, None)
      Field file_list



  ansible_username (True, any, None)
    Username for AXAPI authentication


  skip_backup (False, any, None)
    Skip backup logic


  file (False, any, None)
    aflex local file name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  size (False, any, None)
    aflex file size in byte


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


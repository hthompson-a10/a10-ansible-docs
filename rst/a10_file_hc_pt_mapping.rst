.. _a10_file_hc_pt_mapping_module:


a10_file_hc_pt_mapping -- Configures A10 file.hc-pt-mapping
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

harmony-controller partition tenant mapping






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  file_handle (False, any, None)
    full path of the uploaded file


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


  file (False, any, None)
    harmony-controller local partition tenant mapping file


  action (False, any, None)
    'import'= import; 'export'= export; 'copy'= copy; 'rename'= rename; 'check'= check; 'replace'= replace; 'delete'= delete;


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


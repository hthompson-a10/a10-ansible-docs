.. _a10_file_ca_cert_module:


a10_file_ca_cert -- Configures A10 file.ca-cert
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

ssl certificate file information and management commands






Parameters
----------

  oper (False, any, None)
    Field oper


    file_list (optional, any, None)
      Field file_list


    partition (optional, any, None)
      Field partition



  pfx_password_export (False, any, None)
    The password for exported certificate file (pfx type only)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  pfx_password (False, any, None)
    The password for certificate file (pfx type only)


  file (False, any, None)
    ssl ca certificate local file name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  size (False, any, None)
    ssl ca certificate file size in byte


  ansible_port (True, any, None)
    Port for AXAPI authentication


  file_handle (False, any, None)
    full path of the uploaded file


  uuid (False, any, None)
    uuid of the object


  file_content (False, any, None)
    Content of the uploaded file


  certificate_type (False, any, None)
    'pem'= pem; 'der'= der; 'pfx'= pfx; 'p7b'= p7b;


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


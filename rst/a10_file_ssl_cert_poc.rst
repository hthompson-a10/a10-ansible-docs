.. _a10_file_ssl_cert_poc_module:


a10_file_ssl_cert_poc -- Configures A10 file.ssl-cert-poc
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

ssl certificate file information and management commands






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  file_handle (False, any, None)
    public-key


  file (False, any, None)
    ssl certificate local file name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  file_content (False, any, None)
    Content of the uploaded file


  ansible_password (True, any, None)
    Password for AXAPI authentication


  pfx_password (False, any, None)
    The password for certificate file (pfx type only)


  certificate_type (False, any, None)
    'pem'= pem; 'der'= der; 'pfx'= pfx; 'p7b'= p7b;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  dst_file (False, any, None)
    destination file name for copy and rename action


  action (False, any, None)
    'create'= create; 'import'= import; 'export'= export; 'copy'= copy; 'rename'= rename; 'check'= check; 'replace'= replace; 'delete'= delete;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  size (False, any, None)
    ssl certificate file size in byte









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


.. _a10_file_inspection_global_module:


a10_file_inspection_global -- Configures A10 file.inspection.global
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

File Inspection global commands






Parameters
----------

  max_file_size (False, any, None)
    Maximum file size (bytes) - default 157286400


  ansible_port (True, any, None)
    Port for AXAPI authentication


  max_concurrent_files_action (False, any, None)
    'bypass'= Bypass File Inspection (default);


  uuid (False, any, None)
    uuid of the object


  classification (False, any, None)
    Field classification


    min_classification_len (optional, any, None)
      minimum length to be taken for file classification - default 4096


    classification_disable (optional, any, None)
      Disable Internal File Inspection Classification


    max_classification_len (optional, any, None)
      maximum length to be taken for file classification - default 65536



  ansible_username (True, any, None)
    Username for AXAPI authentication


  file_content (False, any, None)
    Content of the uploaded file


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  max_concurrent_files (False, any, None)
    Max concurrenet inspected files per server - default 10 ( Max concurrenet inspected files per server - default 10)


  max_buffer_size (False, any, None)
    Maximum size (bytes) of content that can be buffered - default 0 (disabled) (Maximum size (bytes) content that can be buffered - default 0 (disabled))


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  logging (False, any, None)
    Field logging


    failed_transactions (optional, any, None)
      'log'= Log event (default); 'no-log'= Do not Log event;


    bypass (optional, any, None)
      Field bypass


    local_logging_disable (optional, any, None)
      Disable local logging



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


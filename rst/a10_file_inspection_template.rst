.. _a10_file_inspection_template_module:


a10_file_inspection_template -- Configures A10 file-inspection.template
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Manage File Inspection template configuration






Parameters
----------

  name (True, any, None)
    file-inspection template name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  inspect (False, any, None)
    Field inspect


    download_icap (optional, any, None)
      respmod icap template (respmod icap Config name)


    inspect_downloads (optional, any, None)
      Inspect file downloads



  downloads_external_suspect_log (False, any, None)
    'log'= Log event (default); 'no-log'= Do not Log event;


  good_uploads_action (False, any, None)
    'reset'= Reset Connection; 'drop'= Drop File; 'allow'= Allow File;


  uploads_suspect_log (False, any, None)
    'log'= Log event (default); 'no-log'= Do not Log event;


  uploads_external_inspect (False, any, None)
    reqmod template for external icap inspection


  downloads_suspect_log (False, any, None)
    'log'= Log event (default); 'no-log'= Do not Log event;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  suspect_downloads_action (False, any, None)
    'reset'= Reset Connection; 'drop'= Drop File; 'allow'= Allow File (default);


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uploads_bad_log (False, any, None)
    'log'= Log event (default); 'no-log'= Do not Log event;


  suspect_uploads_action (False, any, None)
    'reset'= Reset Connection; 'drop'= Drop File; 'allow'= Allow File;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  downloads_external_inspect (False, any, None)
    respmod template for external icap inspection


  ansible_password (True, any, None)
    Password for AXAPI authentication


  good_downloads_action (False, any, None)
    'reset'= Reset Connection; 'drop'= Drop File; 'allow'= Allow File (default);


  bad_uploads_action (False, any, None)
    'reset'= Reset Connection; 'drop'= Drop File; 'allow'= Allow File;


  uploads_external_suspect_log (False, any, None)
    'log'= Log event (default); 'no-log'= Do not Log event;


  bad_downloads_action (False, any, None)
    'reset'= Reset Connection; 'drop'= Drop File (default); 'allow'= Allow File;


  state (True, any, None)
    State of the object to be created.


  downloads_good_log (False, any, None)
    'log'= Log event (default); 'no-log'= Do not Log event;


  user_tag (False, any, None)
    Customized tag


  downloads_bad_log (False, any, None)
    'log'= Log event (default); 'no-log'= Do not Log event;


  uploads_good_log (False, any, None)
    'log'= Log event (default); 'no-log'= Do not Log event;









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


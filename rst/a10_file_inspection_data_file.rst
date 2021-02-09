.. _a10_file_inspection_data_file_module:


a10_file_inspection_data_file -- Configures A10 file.inspection.data-file
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

File Inspection black white list file information and management commands






Parameters
----------

  oper (False, any, None)
    Field oper


    file_list (optional, any, None)
      Field file_list



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ntype (False, any, None)
    data file type


  source_ip_address (False, any, None)
    Source IP address


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (False, any, None)
    data file name


  file_content (False, any, None)
    Content of the uploaded file


  file_url (False, any, None)
    File URL


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    data file action


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


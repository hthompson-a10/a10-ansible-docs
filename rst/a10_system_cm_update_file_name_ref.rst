.. _a10_system_cm_update_file_name_ref_module:


a10_system_cm_update_file_name_ref -- Configures A10 system.cm-update-file-name-ref
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

update the bind name






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  source_name (False, any, None)
    bind source name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  dest_name (False, any, None)
    bind dest name


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  id (False, any, None)
    Specify unique Partition id









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


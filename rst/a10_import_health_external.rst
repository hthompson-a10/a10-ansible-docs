.. _a10_import_health_external_module:


a10_import_health_external -- Configures A10 import.health-external
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Address the External Script Program






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  description (False, any, None)
    Describe the Program Function briefly


  externalfilename (False, any, None)
    Specify the Program Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  remote_file (False, any, None)
    Field remote_file


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  password (False, any, None)
    password for the remote site


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  overwrite (False, any, None)
    Overwrite existing file









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


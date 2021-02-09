.. _a10_import_to_device_module:


a10_import_to_device -- Configures A10 import.to-device
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

specify the target device to import in aVCS






Parameters
----------

  glm_license (False, any, None)
    License File


  ansible_port (True, any, None)
    Port for AXAPI authentication


  web_category_license (False, any, None)
    License file to enable web-category feature


  ansible_username (True, any, None)
    Username for AXAPI authentication


  remote_file (False, any, None)
    profile name for remote url


  glm_cert (False, any, None)
    GLM certificate


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  use_mgmt_port (False, any, None)
    Use management port as source port


  device (False, any, None)
    Device (Device ID)


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


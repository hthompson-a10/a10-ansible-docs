.. _a10_pki_copy_key_module:


a10_pki_copy_key -- Configures A10 pki.copy-key
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Copy SSL key to another file






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  dest_key (False, any, None)
    Destination key file


  src_key (False, any, None)
    Source key file


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  rotation (False, any, None)
    Specify rotation number of SCEP generated key file


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  overwrite (False, any, None)
    Overwrite the destination file if already present









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


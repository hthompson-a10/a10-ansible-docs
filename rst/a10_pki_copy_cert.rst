.. _a10_pki_copy_cert_module:


a10_pki_copy_cert -- Configures A10 pki.copy-cert
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Copy SSL certificate to another file






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  src_cert (False, any, None)
    Source certificate file


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  rotation (False, any, None)
    Specify rotation number of SCEP generated certificate file


  dest_cert (False, any, None)
    Destination certificate file


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


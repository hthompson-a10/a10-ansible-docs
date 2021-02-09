.. _a10_pki_delete_module:


a10_pki_delete -- Configures A10 pki.delete
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Delete SSL cert






Parameters
----------

  oper (False, any, None)
    Field oper


    filename (optional, any, None)
      Field filename



  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ca (False, any, None)
    CA certificate file name


  private_key (False, any, None)
    Private key file name


  state (True, any, None)
    State of the object to be created.


  cert_name (False, any, None)
    Certificate file name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  crl (False, any, None)
    CRL file name


  csr (False, any, None)
    CSR file name









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


.. _a10_import_periodic_ssl_cert_module:


a10_import_periodic_ssl_cert -- Configures A10 import-periodic.ssl-cert
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SSL Cert File(enter bulk when import an archive file)






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ssl_cert (True, any, None)
    SSL Cert File(enter bulk when import an archive file)


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  remote_file (False, any, None)
    profile name for remote url


  pfx_password (False, any, None)
    The password for certificate file (pfx type only)


  period (False, any, None)
    Specify the period in second


  certificate_type (False, any, None)
    'pem'= pem; 'der'= der; 'pfx'= pfx; 'p7b'= p7b;


  state (True, any, None)
    State of the object to be created.


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


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


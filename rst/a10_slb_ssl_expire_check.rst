.. _a10_slb_ssl_expire_check_module:


a10_slb_ssl_expire_check -- Configures A10 slb.ssl-expire-check
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SSL certificate expiration check






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  exception (False, any, None)
    Field exception


    action (optional, any, None)
      'add'= Add an exception; 'delete'= Delete an exception; 'clean'= Delete all exception;


    certificate_name (optional, any, None)
      The certificate name



  expire_address1 (False, any, None)
    Email address for certificate expiration check


  state (True, any, None)
    State of the object to be created.


  ssl_expire_email_address (False, any, None)
    Config Email address for certificate expiration check


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  interval_days (False, any, None)
    The interval of days notice after expiration, default is 2


  before (False, any, None)
    The number of days in advance notice before expiration, default is 5









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


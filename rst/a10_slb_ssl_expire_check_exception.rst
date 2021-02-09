.. _a10_slb_ssl_expire_check_exception_module:


a10_slb_ssl_expire_check_exception -- Configures A10 slb.ssl.expire.check.exception
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Config the exception which will not be checked






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  certificate_name (False, any, None)
    The certificate name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  action (False, any, None)
    'add'= Add an exception; 'delete'= Delete an exception; 'clean'= Delete all exception;


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


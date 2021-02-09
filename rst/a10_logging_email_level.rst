.. _a10_logging_email_level_module:


a10_logging_email_level -- Configures A10 logging.email.level
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set logging level which sent to email address






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


  state (True, any, None)
    State of the object to be created.


  email_levelname (False, any, None)
    'disable'= Do not send log to email address; 'emergency'= System unusable log messages      (severity=0); 'alert'= Action must be taken immediately (severity=1); 'critical'= Critical conditions      (severity=2); 'notification'= Normal but significant conditions (severity=5);


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


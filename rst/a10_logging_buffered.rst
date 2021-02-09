.. _a10_logging_buffered_module:


a10_logging_buffered -- Configures A10 logging.buffered
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set buffered logging parameters






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


  partition_buffersize (False, any, None)
    Logging buffer size (in items), default 3000


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  buffersize (False, any, None)
    Logging buffer size (in items), default 30000


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  levelname (False, any, None)
    'disable'= Do not send log to buffer; 'emergency'= System unusable log messages (severity=0); 'alert'= Action must be taken immediately  (severity=1); 'critical'= Critical conditions               (severity=2); 'error'= Error conditions                  (severity=3); 'warning'= Warning conditions (severity=4); 'notification'= Normal but significant conditions (severity=5); 'information'= Informational messages            (severity=6); 'debugging'= Debug level messages              (severity=7);









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


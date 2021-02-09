.. _a10_logging_email_buffer_module:


a10_logging_email_buffer -- Configures A10 logging.email.buffer
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Logging via email buffering settings






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


  number (False, any, None)
    Number of log messages that can be buffered (Number of log messages that can be buffered, default 50)


  state (True, any, None)
    State of the object to be created.


  time (False, any, None)
    Number of minutes a log message can stay in buffer (Number of minutes a log message can stay in buffer, default 10)


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


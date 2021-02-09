.. _a10_logging_auditlog_module:


a10_logging_auditlog -- Configures A10 logging.auditlog
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set send auditlog to syslog host






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


  ansible_host (True, any, None)
    Host for AXAPI authentication


  host6 (False, any, None)
    Configure the auditlog host


  state (True, any, None)
    State of the object to be created.


  host4 (False, any, None)
    Configure the auditlog host


  audit_facility (False, any, None)
    'local0'= Local use; 'local1'= Local use; 'local2'= Local use; 'local3'= Local use; 'local4'= Local use; 'local5'= Local use; 'local6'= Local use; 'local7'= Local use;  (Configure the facility of auditlog)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  shared (False, any, None)
    Select shared partition


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Set remote audit log port number(Default 514)


  partition_name (False, any, None)
    Select partition name for logging









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


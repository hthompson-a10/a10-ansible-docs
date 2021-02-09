.. _a10_logging_facility_module:


a10_logging_facility -- Configures A10 logging.facility
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Facility parameter for syslog messages






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


  facilityname (False, any, None)
    'local0'= Local use; 'local1'= Local use; 'local2'= Local use; 'local3'= Local use; 'local4'= Local use; 'local5'= Local use; 'local6'= Local use; 'local7'= Local use;  (Facility parameter for syslog messages)


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


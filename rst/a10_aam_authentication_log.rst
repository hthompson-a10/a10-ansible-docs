.. _a10_aam_authentication_log_module:


a10_aam_authentication_log -- Configures A10 aam.authentication.log
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Authentication log configuration






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  enable (False, any, None)
    Enable authentication logs


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  format (False, any, None)
    'syslog'= Syslog Format (default); 'cef'= Common Event Format;


  facility (False, any, None)
    'local0'= Local use; 'local1'= Local use; 'local2'= Local use; 'local3'= Local use; 'local4'= Local use; 'local5'= Local use; 'local6'= Local use; 'local7'= Local use;


  state (True, any, None)
    State of the object to be created.


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


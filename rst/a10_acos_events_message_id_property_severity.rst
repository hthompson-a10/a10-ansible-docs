.. _a10_acos_events_message_id_property_severity_module:


a10_acos_events_message_id_property_severity -- Configures A10 acos.events.message.id.property.severity
=======================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Serverity of log message(s)






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


  message_id_log_msg (optional, any, None)
    Key to identify parent object


  severity_val (False, any, None)
    'emergency'= System unusable log messages (Most Important); 'alert'= Action must be taken immediately; 'critical'= Critical conditions; 'error'= Error conditions; 'warning'= Warning conditions; 'notification'= Normal but significant conditions; 'information'= Informational messages; 'debugging'= Debug level messages (Least Important);


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


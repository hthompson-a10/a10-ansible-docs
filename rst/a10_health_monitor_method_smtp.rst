.. _a10_health_monitor_method_smtp_module:


a10_health_monitor_method_smtp -- Configures A10 health.monitor.method.smtp
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SMTP type






Parameters
----------

  smtp_domain (False, any, None)
    Specify domain name of 'helo' command


  mail_from (False, any, None)
    Specify SMTP Sender


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


  smtp_port (False, any, None)
    Specify SMTP port, default is 25 (Port Number (default 25))


  smtp (False, any, None)
    SMTP type


  ansible_password (True, any, None)
    Password for AXAPI authentication


  rcpt_to (False, any, None)
    Specify SMTP Receiver


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  smtp_starttls (False, any, None)
    Check the STARTTLS support at helo response


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


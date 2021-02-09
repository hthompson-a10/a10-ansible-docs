.. _a10_netflow_monitor_resend_template_module:


a10_netflow_monitor_resend_template -- Configures A10 netflow.monitor.resend-template
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure when to resend netflow template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  monitor_name (optional, any, None)
    Key to identify parent object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  records (False, any, None)
    To resend template once for each number of records (Number of records= default is 1000, 0 means disable template resend based on record-count)


  state (True, any, None)
    State of the object to be created.


  timeout (False, any, None)
    To set time interval to resend template (number of seconds= default is 1800, 0 means disable template resend based on timeout)


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


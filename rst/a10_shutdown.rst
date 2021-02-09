.. _a10_shutdown_module:


a10_shutdown -- Configures A10 shutdown
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Shutdown the System






Parameters
----------

  nin (False, any, None)
    Delay before Shutdown (Time in hours and minutes)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  day_of_month_2 (False, any, None)
    Day of the Month


  month (False, any, None)
    'January'= Month of the year; 'February'= Month of the year; 'March'= Month of the year; 'April'= Month of the year; 'May'= Month of the year; 'June'= Month of the year; 'July'= Month of the year; 'August'= Month of the year; 'September'= Month of the year; 'October'= Month of the year; 'November'= Month of the year; 'December'= Month of the year;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  reason_3 (False, any, None)
    Reason for Shutdown


  reason_2 (False, any, None)
    Reason for Shutdown


  at (False, any, None)
    Shutdown at a specific time/date


  cancel (False, any, None)
    Cancel Pending Shutdown


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  day_of_month (False, any, None)
    Day of the Month


  ansible_port (True, any, None)
    Port for AXAPI authentication


  reason (False, any, None)
    Reason for Shutdown


  state (True, any, None)
    State of the object to be created.


  month_2 (False, any, None)
    'January'= Month of the year; 'February'= Month of the year; 'March'= Month of the year; 'April'= Month of the year; 'May'= Month of the year; 'June'= Month of the year; 'July'= Month of the year; 'August'= Month of the year; 'September'= Month of the year; 'October'= Month of the year; 'November'= Month of the year; 'December'= Month of the year;


  time (False, any, None)
    Time to Shutdown (hh=mm)


  ansible_password (True, any, None)
    Password for AXAPI authentication









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


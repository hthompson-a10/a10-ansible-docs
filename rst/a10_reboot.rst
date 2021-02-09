.. _a10_reboot_module:


a10_reboot -- Configures A10 reboot
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Reboot the System






Parameters
----------

  all (False, any, None)
    Reboot all devices when VCS is enabled, or only this device itself if VCS is not enabled


  nin (False, any, None)
    Reboot after a time interval (Time in hours and minutes)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  day_of_month_2 (False, any, None)
    Day of the Month


  month (False, any, None)
    'January'= Month of the year; 'February'= Month of the year; 'March'= Month of the year; 'April'= Month of the year; 'May'= Month of the year; 'June'= Month of the year; 'July'= Month of the year; 'August'= Month of the year; 'September'= Month of the year; 'October'= Month of the year; 'November'= Month of the year; 'December'= Month of the year;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  reason (False, any, None)
    Reason for Reboot


  reason_2 (False, any, None)
    Reason for Reboot


  at (False, any, None)
    Reboot at a Specific time/date


  device (False, any, None)
    Reboot a specific device when VCS is enabled (device id)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  day_of_month (False, any, None)
    Day of the Month


  ansible_port (True, any, None)
    Port for AXAPI authentication


  reason_3 (False, any, None)
    Reason for Reboot


  state (True, any, None)
    State of the object to be created.


  month_2 (False, any, None)
    'January'= Month of the year; 'February'= Month of the year; 'March'= Month of the year; 'April'= Month of the year; 'May'= Month of the year; 'June'= Month of the year; 'July'= Month of the r; 'August'= Month of the year; 'September'= Month of the year; 'October'= Month of the year; 'November'= Month of the year; 'December'= Month of the year;


  time (False, any, None)
    Time to Reboot (hh=mm)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  cancel (False, any, None)
    Cancel Pending Reboot









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


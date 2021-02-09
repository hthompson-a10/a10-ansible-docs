.. _a10_clock_set_module:


a10_clock_set -- Configures A10 clock.set
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set the Time and Date






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  time_cfg (False, any, None)
    Field time_cfg


    month_2 (optional, any, None)
      'January'= Month of the year; 'February'= Month of the year; 'March'= Month of the year; 'April'= Month of the year; 'May'= Month of the year; 'June'= Month of the year; 'July'= Month of the year; 'August'= Month of the year; 'September'= Month of the year; 'October'= Month of the year; 'November'= Month of the year; 'December'= Month of the year;


    time (optional, any, None)
      Current Time


    day_of_month_2 (optional, any, None)
      Day of the Month


    year (optional, any, None)
      Year


    day_of_month (optional, any, None)
      Day of the Month


    month (optional, any, None)
      'January'= Month of the year; 'February'= Month of the year; 'March'= Month of the year; 'April'= Month of the year; 'May'= Month of the year; 'June'= Month of the year; 'July'= Month of the year; 'August'= Month of the year; 'September'= Month of the year; 'October'= Month of the year; 'November'= Month of the year; 'December'= Month of the year;



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


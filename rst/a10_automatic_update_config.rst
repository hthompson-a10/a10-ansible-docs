.. _a10_automatic_update_config_module:


a10_automatic_update_config -- Configures A10 automatic-update.config
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure software update schedule






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


  schedule (False, any, None)
    Field schedule


  day_time (False, any, None)
    Time of day to update (hh=mm) in 24 hour local time


  daily (False, any, None)
    Every day


  state (True, any, None)
    State of the object to be created.


  week_day (False, any, None)
    'Monday'= Monday; 'Tuesday'= Tuesday; 'Wednesday'= Wednesday; 'Thursday'= Thursday; 'Friday'= Friday; 'Saturday'= Saturday; 'Sunday'= Sunday;


  feature_name (True, any, None)
    'app-fw'= Application Firewall Configuration;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  week_time (False, any, None)
    Time of day to update (hh=mm) in 24 hour local time


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  weekly (False, any, None)
    Every week









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


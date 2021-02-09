.. _a10_license_manager_module:


a10_license_manager -- Configures A10 license-manager
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure license manager






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  host_list (False, any, None)
    Field host_list


    host_ipv6 (optional, any, None)
      Configure license manager server ipv6-address


    port (optional, any, None)
      Configure the license manager port, default is 443


    host_ipv4 (optional, any, None)
      license server ip address (length=1-31)


    uuid (optional, any, None)
      uuid of the object



  connect (False, any, None)
    Field connect


    connect (optional, any, None)
      Connect to license manager to activate


    uuid (optional, any, None)
      uuid of the object



  use_mgmt_port (False, any, None)
    Use management port to connect license server


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  bandwidth_unrestricted (False, any, None)
    Set the bandwidth to maximum


  instance_name (False, any, None)
    Configure instance name [format= (string).(string).(string).(string)]


  ansible_port (True, any, None)
    Port for AXAPI authentication


  bandwidth_base (False, any, None)
    Configure feature bandwidth base (Mb)


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  interval (False, any, None)
    Configure interval profile (1 monthly, 2 daily, 3 hourly)


  overage (False, any, None)
    Field overage


    kb (optional, any, None)
      Number of KB


    uuid (optional, any, None)
      uuid of the object


    mb (optional, any, None)
      Number of MB


    seconds (optional, any, None)
      Number of seconds


    bytes (optional, any, None)
      Number of bytes


    days (optional, any, None)
      Number of days


    hours (optional, any, None)
      Number of hours


    gb (optional, any, None)
      Number of GB


    minutes (optional, any, None)
      Number of minutes



  state (True, any, None)
    State of the object to be created.


  sn (False, any, None)
    serial number


  reminder_list (False, any, None)
    Field reminder_list


    uuid (optional, any, None)
      uuid of the object


    reminder_value (optional, any, None)
      Configure reminder for grace time (Hour)










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


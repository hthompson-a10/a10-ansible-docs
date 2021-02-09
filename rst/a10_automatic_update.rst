.. _a10_automatic_update_module:


a10_automatic_update -- Configures A10 automatic-update
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Automatic update configuration






Parameters
----------

  reset (False, any, None)
    Field reset


    feature_name (optional, any, None)
      'app-fw'= Application Firewall;



  proxy_server (False, any, None)
    Field proxy_server


    auth_type (optional, any, None)
      'ntlm'= NTLM authentication(default); 'basic'= Basic authentication;


    username (optional, any, None)
      Username for proxy authentication


    domain (optional, any, None)
      Realm for NTLM authentication


    https_port (optional, any, None)
      Proxy server HTTPs port


    secret_string (optional, any, None)
      password value


    encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


    proxy_host (optional, any, None)
      Proxy server hostname or IP address


    password (optional, any, None)
      Password for proxy authentication


    uuid (optional, any, None)
      uuid of the object



  ansible_username (True, any, None)
    Username for AXAPI authentication


  config_list (False, any, None)
    Field config_list


    day_time (optional, any, None)
      Time of day to update (hh=mm) in 24 hour local time


    uuid (optional, any, None)
      uuid of the object


    schedule (optional, any, None)
      Field schedule


    daily (optional, any, None)
      Every day


    week_day (optional, any, None)
      'Monday'= Monday; 'Tuesday'= Tuesday; 'Wednesday'= Wednesday; 'Thursday'= Thursday; 'Friday'= Friday; 'Saturday'= Saturday; 'Sunday'= Sunday;


    feature_name (optional, any, None)
      'app-fw'= Application Firewall Configuration;


    week_time (optional, any, None)
      Time of day to update (hh=mm) in 24 hour local time


    weekly (optional, any, None)
      Every week



  use_mgmt_port (False, any, None)
    Use management port to connect


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  info (False, any, None)
    Field info


    uuid (optional, any, None)
      uuid of the object



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  checknow (False, any, None)
    Field checknow


    uuid (optional, any, None)
      uuid of the object



  revert (False, any, None)
    Field revert


    feature_name (optional, any, None)
      'app-fw'= Application Firewall;



  state (True, any, None)
    State of the object to be created.


  check_now (False, any, None)
    Field check_now


    feature_name (optional, any, None)
      'app-fw'= Application Firewall;



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


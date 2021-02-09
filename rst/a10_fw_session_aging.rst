.. _a10_fw_session_aging_module:


a10_fw_session_aging -- Configures A10 fw.session-aging
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Session aging






Parameters
----------

  icmp_idle_timeout (False, any, None)
    Idle Timeout time (default 2 seconds) (Second, default 2)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  name (True, any, None)
    session-aging Template (session-aging Template name)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  udp (False, any, None)
    Field udp


    udp_idle_timeout (optional, any, None)
      Idle Timeout (sec), default is 120 (number)


    uuid (optional, any, None)
      uuid of the object


    port_cfg (optional, any, None)
      Field port_cfg



  tcp (False, any, None)
    Field tcp


    half_close_idle_timeout (optional, any, None)
      TCP Half Close Idle Timeout (sec), default is off (number)


    uuid (optional, any, None)
      uuid of the object


    tcp_idle_timeout (optional, any, None)
      Idle Timeout (sec), default is 600 (number)


    force_delete_timeout_100ms (optional, any, None)
      The maximum time that a session can stay in the system before being deleted, default is off (number in 100ms)


    half_open_idle_timeout (optional, any, None)
      TCP Half Open Idle Timeout (sec), default is off (number)


    port_cfg (optional, any, None)
      Field port_cfg


    force_delete_timeout (optional, any, None)
      The maximum time that a session can stay in the system before being deleted, default is off (number (second))



  state (True, any, None)
    State of the object to be created.


  ip_idle_timeout (False, any, None)
    Idle Timeout time(sec), default is 30 (Second)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object









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


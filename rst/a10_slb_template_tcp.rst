.. _a10_slb_template_tcp_module:


a10_slb_template_tcp -- Configures A10 slb.template.tcp
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

L4 TCP switch config






Parameters
----------

  lan_fast_ack (False, any, None)
    Enable fast TCP ack on LAN


  ansible_username (True, any, None)
    Username for AXAPI authentication


  initial_window_size (False, any, None)
    Set the initial window size (number)


  down (False, any, None)
    send reset to client when server is down


  reset_fwd (False, any, None)
    send reset to server if error happens


  disable (False, any, None)
    send reset to client when server is disabled


  del_session_on_server_down (False, any, None)
    Delete session if the server/port goes down (either disabled/hm down)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  qos (False, any, None)
    QOS level (number)


  half_open_idle_timeout (False, any, None)
    TCP Half Open Idle Timeout (sec), default off (half open idle timeout in second, default off)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  insert_client_ip (False, any, None)
    Insert client ip into TCP option


  name (True, any, None)
    Fast TCP Template Name


  ansible_port (True, any, None)
    Port for AXAPI authentication


  logging (False, any, None)
    'init'= init only log; 'term'= termination only log; 'both'= both initial and termination log;


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  idle_timeout (False, any, None)
    Idle Timeout value (Interval of 60 seconds), default 120 seconds (idle timeout in second, default 120)


  alive_if_active (False, any, None)
    keep connection alive if active traffic


  half_close_idle_timeout (False, any, None)
    TCP Half Close Idle Timeout (sec), default off (half close idle timeout in second, default off)


  state (True, any, None)
    State of the object to be created.


  reset_follow_fin (False, any, None)
    send reset to client or server upon receiving first fin


  reset_rev (False, any, None)
    send reset to client if error happens


  force_delete_timeout_100ms (False, any, None)
    The maximum time that a session can stay in the system before being delete (number in 100ms)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  force_delete_timeout (False, any, None)
    The maximum time that a session can stay in the system before being delete (number (second))









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


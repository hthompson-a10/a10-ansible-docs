.. _a10_web_service_module:


a10_web_service -- Configures A10 web-service
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure Web Services






Parameters
----------

  secure (False, any, None)
    Field secure


    private_key (optional, any, None)
      Field private_key


    certificate (optional, any, None)
      Field certificate


    regenerate (optional, any, None)
      Field regenerate


    generate (optional, any, None)
      Field generate


    restart (optional, any, None)
      Restart WEB service


    wipe (optional, any, None)
      Wipe WEB private-key and certificate



  server_disable (False, any, None)
    Disable


  ansible_username (True, any, None)
    Username for AXAPI authentication


  axapi_idle (False, any, None)
    Idle timeout of a xml service connection in minutes (Connection idle timeout value in minutes, default 10, 0 means never timeout)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Set Web Server Port (Port number(default 80))


  auto_redirt_disable (False, any, None)
    Diable


  axapi_session_limit (False, any, None)
    Set the max allowed aXAPI sessions (Session limit (default 30))


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  gui_idle (False, any, None)
    Idle timeout of a connection in minutes (Connection idle timeout value in minutes, default 10, 0 means never timeout)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  secure_port (False, any, None)
    Set web secure server port number for listening (Secure Port Number(default 443))


  secure_server_disable (False, any, None)
    Disable


  login_message (False, any, None)
    Set GUI login message


  ansible_password (True, any, None)
    Password for AXAPI authentication


  gui_session_limit (False, any, None)
    Set the max allowed GUI sessions (Session limit (default 30))









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


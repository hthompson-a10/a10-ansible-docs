.. _a10_glm_proxy_server_module:


a10_glm_proxy_server -- Configures A10 glm.proxy-server
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Connect to GLM through proxy server






Parameters
----------

  username (False, any, None)
    Username for proxy authentication


  secret_string (False, any, None)
    password value


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  state (True, any, None)
    State of the object to be created.


  ansible_host (True, any, None)
    Host for AXAPI authentication


  host (False, any, None)
    Proxy server hostname or IP address


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  password (False, any, None)
    Password for proxy authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Proxy server port









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


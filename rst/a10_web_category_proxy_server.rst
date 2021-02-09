.. _a10_web_category_proxy_server_module:


a10_web_category_proxy_server -- Configures A10 web.category.proxy-server
=========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Commands to connect web-category through proxy server






Parameters
----------

  auth_type (False, any, None)
    'ntlm'= NTLM authentication(default); 'basic'= Basic authentication;


  username (False, any, None)
    Username for proxy authentication


  domain (False, any, None)
    Realm for NTLM authentication


  https_port (False, any, None)
    Proxy server HTTPS port(HTTP port will be used if not configured)


  secret_string (False, any, None)
    password value


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  password (False, any, None)
    Password for proxy authentication


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  http_port (False, any, None)
    Proxy server HTTP port


  uuid (False, any, None)
    uuid of the object


  proxy_host (False, any, None)
    Proxy server hostname or IP address


  ansible_username (True, any, None)
    Username for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


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


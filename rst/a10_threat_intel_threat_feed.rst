.. _a10_threat_intel_threat_feed_module:


a10_threat_intel_threat_feed -- Configures A10 threat-intel.threat-feed
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure vendor specific module control options






Parameters
----------

  secret_string (False, any, None)
    password value


  domain (False, any, None)
    Realm for NTLM authentication


  enable (False, any, None)
    Enable module


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  rtu_update_disable (False, any, None)
    Disables real time updates(default enable)


  ntype (True, any, None)
    'webroot'= Configure Webroot module options;


  proxy_password (False, any, None)
    Password for proxy authentication


  proxy_port (False, any, None)
    Port to connect on proxy server


  use_mgmt_port (False, any, None)
    Use management interface for all communication with threat-intel server


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  server (False, any, None)
    Server IP or Hostname


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    Port to query server(default 443)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  server_timeout (False, any, None)
    Server Timeout in seconds (default= 15s)


  log_level (False, any, None)
    'disable'= Disable all logging; 'error'= Log error events; 'warning'= Log warning events and above; 'info'= Log info events and above; 'debug'= Log debug events and above; 'trace'= enable all logs;


  uuid (False, any, None)
    uuid of the object


  proxy_host (False, any, None)
    Proxy server hostname or IP address


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  proxy_username (False, any, None)
    Username for proxy authentication


  update_interval (False, any, None)
    Interval to check for database or RTU updates(default 120 mins)


  user_tag (False, any, None)
    Customized tag


  proxy_auth_type (False, any, None)
    'ntlm'= NTLM authentication(default); 'basic'= Basic authentication;









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


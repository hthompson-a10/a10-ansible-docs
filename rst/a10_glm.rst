.. _a10_glm_module:


a10_glm -- Configures A10 glm
=============================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set GLM Connection values






Parameters
----------

  proxy_server (False, any, None)
    Field proxy_server


    username (optional, any, None)
      Username for proxy authentication


    secret_string (optional, any, None)
      password value


    host (optional, any, None)
      Proxy server hostname or IP address


    uuid (optional, any, None)
      uuid of the object


    encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


    password (optional, any, None)
      Password for proxy authentication


    port (optional, any, None)
      Proxy server port



  ansible_username (True, any, None)
    Username for AXAPI authentication


  enable_requests (False, any, None)
    Turn on periodic GLM license requests (default license retrieval interval is every 24 hours)


  allocate_bandwidth (False, any, None)
    Enter the requested bandwidth in Mbps for Capacity Pool


  use_mgmt_port (False, any, None)
    Use management port to connect to GLM


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  port (False, any, None)
    License request port (default 443)


  appliance_name (False, any, None)
    Helpful identifier for this appliance


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  interval (False, any, None)
    GLM license request interval (in hours)


  token (False, any, None)
    License entitlement token


  send (False, any, None)
    Field send


    license_request (optional, any, None)
      Immediately send a single GLM license request



  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  enterprise (False, any, None)
    Enter the ELM hostname or IP


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


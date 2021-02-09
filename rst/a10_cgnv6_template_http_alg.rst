.. _a10_cgnv6_template_http_alg_module:


a10_cgnv6_template_http_alg -- Configures A10 cgnv6.template.http-alg
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

HTTP-ALG Template






Parameters
----------

  header_name_client_ip (False, any, None)
    Header name (default= X-Forwarded-For)


  secret_string (False, any, None)
    The RADIUS secret


  timeout (False, any, None)
    The maximum time allowed for waiting for a response from a radius server (default 2)


  header_name_msisdn (False, any, None)
    Header name (default= X-MSISDN)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  request_insert_client_ip (False, any, None)
    Insert Client IP into HTTP request


  retry_svr_num (False, any, None)
    Specify the maximum RADIUS servers allowed to try (default 0)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    HTTP-ALG template name


  ansible_port (True, any, None)
    Port for AXAPI authentication


  retry (False, any, None)
    Specify the maximum retries allowed for sending an request to a RADIUS server (default 2) (The maximum retries allowed for sending an request to the radius server (default 2))


  uuid (False, any, None)
    uuid of the object


  include_tunnel_ip (False, any, None)
    Include the tunnel IP (applies to DS-Lite and 6RD-NAT64 sessions)


  request_insert_msisdn (False, any, None)
    Insert MSISDN into HTTP request


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  radius_sg (False, any, None)
    RADIUS service group (RADIUS service group name)


  user_tag (False, any, None)
    Customized tag


  method (False, any, None)
    'append'= Append if there is already a header (default); 'replace'= Replace if there is already a header;









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


.. _a10_slb_template_server_ssh_module:


a10_slb_template_server_ssh -- Configures A10 slb.template.server-ssh
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Server Side SSH Template






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'successful_handshakes'= successful_handshakes; 'failed_handshakes'= failed_handshakes; 'forwarding_errors'= forwarding_errors;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  forward_proxy_enable (False, any, None)
    Enable SSH forward proxy


  name (True, any, None)
    Server SSH Template Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  stats (False, any, None)
    Field stats


    forwarding_errors (optional, any, None)
      Field forwarding_errors


    successful_handshakes (optional, any, None)
      Field successful_handshakes


    failed_handshakes (optional, any, None)
      Field failed_handshakes


    name (optional, any, None)
      Server SSH Template Name



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


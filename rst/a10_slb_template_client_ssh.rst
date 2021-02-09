.. _a10_slb_template_client_ssh_module:


a10_slb_template_client_ssh -- Configures A10 slb.template.client-ssh
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Client Side SSH Template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  forward_proxy_enable (False, any, None)
    Enable SSH forward proxy


  name (True, any, None)
    Client SSH Template Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  forward_proxy_hostkey (False, any, None)
    Specify private-key (Key Name)


  state (True, any, None)
    State of the object to be created.


  passphrase (False, any, None)
    Password Phrase


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
      Client SSH Template Name



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


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


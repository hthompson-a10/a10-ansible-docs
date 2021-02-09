.. _a10_slb_ssl_forward_proxy_cert_module:


a10_slb_ssl_forward_proxy_cert -- Configures A10 slb.ssl-forward-proxy-cert
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Show hashed certificates






Parameters
----------

  oper (False, any, None)
    Field oper


    vserver (optional, any, None)
      virtual server name


    server_ip (optional, any, None)
      IPv4 or IPv6 address of the server


    hashed_certificate (optional, any, None)
      Field hashed_certificate


    server_name (optional, any, None)
      Name of the server


    port (optional, any, None)
      Virtual Port


    server_port (optional, any, None)
      Port of the server



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication









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


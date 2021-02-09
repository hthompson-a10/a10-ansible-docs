.. _a10_tacacs_server_host_tacacs_hostname_module:


a10_tacacs_server_host_tacacs_hostname -- Configures A10 tacacs-server.host.tacacs-hostname
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify the hostname of TACACS+ server






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  hostname (True, any, None)
    Hostname of TACACS+ server


  state (True, any, None)
    State of the object to be created.


  secret (False, any, None)
    Field secret


    source_trunk (optional, any, None)
      Trunk interface (Trunk interface number)


    source_lif (optional, any, None)
      Logical interface (Lif interface number)


    source_ve (optional, any, None)
      Virtual ethernet interface (Virtual ethernet interface number)


    encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) help-val The ENCRYPTED secret string


    source_loopback (optional, any, None)
      Loopback interface (Port number)


    source_ip (optional, any, None)
      IP address


    secret_value (optional, any, None)
      The TACACS+ server's secret


    source_ipv6 (optional, any, None)
      IPV6 address


    source_eth (optional, any, None)
      Ethernet interface (Port number)


    port_cfg (optional, any, None)
      Field port_cfg



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


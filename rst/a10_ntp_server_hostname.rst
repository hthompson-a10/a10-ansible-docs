.. _a10_ntp_server_hostname_module:


a10_ntp_server_hostname -- Configures A10 ntp.server.hostname
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IPV4 address, IPV6 address or host name of NTP server






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


  prefer (False, any, None)
    Set this NTP server as preferred


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  host_servername (True, any, None)
    IPV4 address, IPV6 address or host name of NTP server(string1~63)


  key (False, any, None)
    Use trusted key to authenticate this NTP server (The trusted key number to use)


  action (False, any, None)
    'enable'= Enable this NTP server; 'disable'= Disable this NTP server;


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


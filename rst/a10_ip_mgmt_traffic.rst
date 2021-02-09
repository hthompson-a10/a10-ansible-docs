.. _a10_ip_mgmt_traffic_module:


a10_ip_mgmt_traffic -- Configures A10 ip.mgmt-traffic
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Management traffic IP parameters






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


  state (True, any, None)
    State of the object to be created.


  source_interface (False, any, None)
    Field source_interface


    lif (optional, any, None)
      Logical interface (Lif interface number)


    ve (optional, any, None)
      Virtual ethernet interface (Virtual ethernet interface number)


    loopback (optional, any, None)
      Loopback interface (Port number)


    tunnel (optional, any, None)
      Tunnel interface (Tunnel interface number)


    ethernet (optional, any, None)
      Ethernet interface (Port number)


    trunk (optional, any, None)
      Trunk interface (Trunk interface number)



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  traffic_type (True, any, None)
    'all'= All; 'ftp'= FTP; 'ntp'= NTP; 'snmp-trap'= SNMP Trap; 'ssh'= SSH and SCP; 'syslog'= SYSLOG; 'telnet'= Telnet; 'tftp'= TFTP; 'web'= Web - HTTP and HTTPS;


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


.. _a10_fw_alg_module:


a10_fw_alg -- Configures A10 fw.alg
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure ALG






Parameters
----------

  ftp (False, any, None)
    Field ftp


    sampling_enable (optional, any, None)
      Field sampling_enable


    default_port_disable (optional, any, None)
      'default-port-disable'= Disable FTP ALG default port 21;


    uuid (optional, any, None)
      uuid of the object



  ansible_port (True, any, None)
    Port for AXAPI authentication


  sip (False, any, None)
    Field sip


    sampling_enable (optional, any, None)
      Field sampling_enable


    default_port_disable (optional, any, None)
      'default-port-disable'= Disable SIP ALG default port 5060;


    uuid (optional, any, None)
      uuid of the object



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  pptp (False, any, None)
    Field pptp


    sampling_enable (optional, any, None)
      Field sampling_enable


    default_port_disable (optional, any, None)
      'default-port-disable'= Disable PPTP ALG default port 1723;


    uuid (optional, any, None)
      uuid of the object



  ansible_password (True, any, None)
    Password for AXAPI authentication


  rtsp (False, any, None)
    Field rtsp


    sampling_enable (optional, any, None)
      Field sampling_enable


    default_port_disable (optional, any, None)
      'default-port-disable'= Disable RTSP ALG default port 554;


    uuid (optional, any, None)
      uuid of the object



  state (True, any, None)
    State of the object to be created.


  dns (False, any, None)
    Field dns


    default_port_disable (optional, any, None)
      'default-port-disable'= Disable DNS ALG default port 53;


    uuid (optional, any, None)
      uuid of the object



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  tftp (False, any, None)
    Field tftp


    sampling_enable (optional, any, None)
      Field sampling_enable


    default_port_disable (optional, any, None)
      'default-port-disable'= Disable TFTP ALG default port 69;


    uuid (optional, any, None)
      uuid of the object



  icmp (False, any, None)
    Field icmp


    disable (optional, any, None)
      'disable'= Disable ICMP ALG which allows ICMP errors to pass the firewall;


    uuid (optional, any, None)
      uuid of the object



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


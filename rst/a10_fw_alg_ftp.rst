.. _a10_fw_alg_ftp_module:


a10_fw_alg_ftp -- Configures A10 fw.alg.ftp
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change Firewall FTP ALG Settings






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'client-port-request'= PORT Requests From Client; 'client-eprt- request'= EPRT Requests From Client; 'server-pasv-reply'= PASV Replies From Server; 'server-epsv-reply'= EPSV Replies From Server; 'port-retransmits'= PORT Retransmits; 'pasv-retransmits'= PASV Retransmits; 'smp-app-type-mismatch'= SMP App Type Mismatch; 'retransmit-sanity-check-failure'= Retransmit Sanity Check Failure; 'smp-conn-alloc-failure'= SMP Helper Conn Alloc Failure; 'port-helper- created'= PORT Helper Created; 'pasv-helper-created'= PASV Helper Created; 'port-helper-acquire-in-del-q'= PORT Helper Acquire In Del Queue; 'port-helper- acquire-already-used'= PORT Helper Acquire Already Used; 'pasv-helper-acquire- in-del-q'= PASV Helper Acquire In Del Queue; 'pasv-helper-acquire-already- used'= PASV Helper Acquire Already Used; 'port-helper-freed-used'= PORT Helper Freed Used; 'port-helper-freed-unused'= PORT Helper Freed Unused; 'pasv-helper- freed-used'= PASV Helper Freed Used; 'pasv-helper-freed-unused'= PASV Helper Freed Unused;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    client_port_request (optional, any, None)
      PORT Requests From Client


    client_eprt_request (optional, any, None)
      EPRT Requests From Client


    server_epsv_reply (optional, any, None)
      EPSV Replies From Server


    server_pasv_reply (optional, any, None)
      PASV Replies From Server



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  default_port_disable (False, any, None)
    'default-port-disable'= Disable FTP ALG default port 21;


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


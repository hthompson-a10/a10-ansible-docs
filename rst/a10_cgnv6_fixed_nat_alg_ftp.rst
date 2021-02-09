.. _a10_cgnv6_fixed_nat_alg_ftp_module:


a10_cgnv6_fixed_nat_alg_ftp -- Configures A10 cgnv6.fixed.nat.alg.ftp
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change Fixed NAT FTP ALG Settings






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'port-requests'= PORT Requests From Client; 'eprt-requests'= EPRT Requests From Client; 'lprt-requests'= LPRT Requests From Client; 'pasv- replies'= PASV Replies From Server; 'epsv-replies'= EPSV Replies From Server; 'lpsv-replies'= LPSV Replies From Server; 'port-retransmits'= Port Mode Request Retransmits; 'pasv-retransmits'= Passive Mode Reply Retransmits; 'port-helper- created'= Port Mode Helper Created; 'pasv-helper-created'= Passive Mode Helper Created; 'port-helper-freed'= Port Mode Helper Freed; 'pasv-helper-freed'= Passive Mode Helper Freed; 'port-helper-unused'= Port Mode Helper Unused; 'pasv-helper-unused'= Passive Mode Helper Unused; 'port-helper-creation- failure'= Port Helper Creation Failure; 'pasv-helper-creation-failure'= Passive Helper Creation Failure; 'get-conn-ext-failure'= Get Conn Extension Failure; 'smp-app-type-mismatch'= SMP ALG App Type Mismatch;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    pasv_replies (optional, any, None)
      PASV Replies From Server


    epsv_replies (optional, any, None)
      EPSV Replies From Server


    lpsv_replies (optional, any, None)
      LPSV Replies From Server


    port_requests (optional, any, None)
      PORT Requests From Client


    eprt_requests (optional, any, None)
      EPRT Requests From Client


    lprt_requests (optional, any, None)
      LPRT Requests From Client



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


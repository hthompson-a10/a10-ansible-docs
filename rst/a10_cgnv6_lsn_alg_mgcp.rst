.. _a10_cgnv6_lsn_alg_mgcp_module:


a10_cgnv6_lsn_alg_mgcp -- Configures A10 cgnv6.lsn.alg.mgcp
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change LSN MGCP ALG Settings






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'auep'= MGCP AUEP; 'aucx'= MGCP AUCX; 'crcx'= MGCP CRCX; 'dlcx'= MGCP DLCX; 'epcf'= MGCP EPCF; 'mdcx'= MGCP MDCX; 'ntfy'= MGCP NTFY; 'rqnt'= MGCP RQNT; 'rsip'= MGCP RSIP; 'parse-error'= MGCP Message Parse Error; 'conn- ext-creation-failure'= MGCP Create Connection Extension Failure; 'third-party- sdp'= MGCP Third-Party SDP; 'sdp-process-candidate-failure'= MGCP Operate SDP Media Candidate Attribute Failure; 'sdp-op-failure'= MGCP Operate SDP Failure; 'sdp-alloc-port-map-success'= MGCP Alloc SDP Port Map Success; 'sdp-alloc-port- map-failure'= MGCP Alloc SDP Port Map Failure; 'modify-failure'= MGCP Message Modify Failure; 'rewrite-failure'= MGCP Message Rewrite Failure; 'tcp-out-of- order-drop'= TCP Out-of-Order Drop;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    auep (optional, any, None)
      MGCP AUEP


    mdcx (optional, any, None)
      MGCP MDCX


    rsip (optional, any, None)
      MGCP RSIP


    rqnt (optional, any, None)
      MGCP RQNT


    ntfy (optional, any, None)
      MGCP NTFY


    crcx (optional, any, None)
      MGCP CRCX


    dlcx (optional, any, None)
      MGCP DLCX


    epcf (optional, any, None)
      MGCP EPCF


    aucx (optional, any, None)
      MGCP AUCX



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  mgcp_value (False, any, None)
    'enable'= Enable MGCP ALG for LSN;









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


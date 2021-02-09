.. _a10_slb_ftp_ctl_module:


a10_slb_ftp_ctl -- Configures A10 slb.ftp-ctl
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure FTP






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'sessions_num'= Total Control Sessions; 'alg_pkts_num'= Total ALG packets; 'alg_pkts_xmitted_num'= ALG packets rexmitted; 'alg_port_helper_created'= Total PORT helper sessions; 'alg_pasv_helper_created'= Total PASV helper sessions; 'alg_port_helper_freed_unused'= PORT helper freed unused; 'alg_pasv_helper_freed_unused'= PASV helper freed unused; 'alg_port_helper_nat_free'= PORT helper NAT free;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    alg_pkts_xmitted_num (optional, any, None)
      ALG packets rexmitted


    alg_pasv_helper_freed_unused (optional, any, None)
      PASV helper freed unused


    alg_pasv_helper_created (optional, any, None)
      Total PASV helper sessions


    alg_port_helper_created (optional, any, None)
      Total PORT helper sessions


    sessions_num (optional, any, None)
      Total Control Sessions


    alg_port_helper_nat_free (optional, any, None)
      PORT helper NAT free


    alg_port_helper_freed_unused (optional, any, None)
      PORT helper freed unused


    alg_pkts_num (optional, any, None)
      Total ALG packets



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


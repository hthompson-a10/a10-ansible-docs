.. _a10_slb_mysql_module:


a10_slb_mysql -- Configures A10 slb.mysql
=========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure mysql






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'curr_proxy'= Curr Proxy Conns; 'total_proxy'= Total Proxy Conns; 'curr_be_enc'= Curr BE Encryption Conns; 'total_be_enc'= Total BE Encryption Conns; 'curr_fe_enc'= Curr FE Encryption Conns; 'total_fe_enc'= Total FE Encryption Conns; 'client_fin'= Client FIN; 'server_fin'= Server FIN; 'session_err'= Session err; 'queries'= DB Queries; 'commands'= DB commands reply;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    server_fin (optional, any, None)
      Server FIN


    curr_be_enc (optional, any, None)
      Curr BE Encryption Conns


    total_be_enc (optional, any, None)
      Total BE Encryption Conns


    total_proxy (optional, any, None)
      Total Proxy Conns


    curr_proxy (optional, any, None)
      Curr Proxy Conns


    commands (optional, any, None)
      DB commands reply


    client_fin (optional, any, None)
      Client FIN


    curr_fe_enc (optional, any, None)
      Curr FE Encryption Conns


    queries (optional, any, None)
      DB Queries


    session_err (optional, any, None)
      Session err


    total_fe_enc (optional, any, None)
      Total FE Encryption Conns



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


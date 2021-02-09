.. _a10_cgnv6_lsn_performance_module:


a10_cgnv6_lsn_performance -- Configures A10 cgnv6.lsn.performance
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Large-Scale NAT performance statistics






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'data-sessions-current-epoch'= data-sessions-current-epoch; 'fullcone-created-current-epoch'= fullcone-created-current-epoch; 'user-quote- created-current-epoch'= user-quote-created-current-epoch; 'data-sessions- previous-epoch-first'= data-sessions-previous-epoch-first; 'fullcone-created- previous-epoch-first'= fullcone-created-previous-epoch-first; 'user-quote- created-previous-epoch-first'= user-quote-created-previous-epoch-first; 'data- sessions-previous-epoch-last'= data-sessions-previous-epoch-last; 'fullcone- created-previous-epoch-last'= fullcone-created-previous-epoch-last; 'user- quote-created-previous-epoch-last'= user-quote-created-previous-epoch-last;



  oper (False, any, None)
    Field oper


    data_sessions (optional, any, None)
      Field data_sessions


    full_cone_sessions (optional, any, None)
      Field full_cone_sessions


    user_quotas (optional, any, None)
      Field user_quotas



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    data_sessions_previous_epoch_first (optional, any, None)
      Field data_sessions_previous_epoch_first


    user_quote_created_previous_epoch_first (optional, any, None)
      Field user_quote_created_previous_epoch_first


    fullcone_created_previous_epoch_first (optional, any, None)
      Field fullcone_created_previous_epoch_first


    user_quote_created_previous_epoch_last (optional, any, None)
      Field user_quote_created_previous_epoch_last


    data_sessions_previous_epoch_last (optional, any, None)
      Field data_sessions_previous_epoch_last


    data_sessions_current_epoch (optional, any, None)
      Field data_sessions_current_epoch


    fullcone_created_current_epoch (optional, any, None)
      Field fullcone_created_current_epoch


    user_quote_created_current_epoch (optional, any, None)
      Field user_quote_created_current_epoch


    fullcone_created_previous_epoch_last (optional, any, None)
      Field fullcone_created_previous_epoch_last



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


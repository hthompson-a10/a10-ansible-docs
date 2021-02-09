.. _a10_slb_ftp_data_module:


a10_slb_ftp_data -- Configures A10 slb.ftp-data
===============================================

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
      'all'= all; 'sessions_num'= Total Data Sessions; 'port_out_of_range'= Drop Data Port out of range;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    sessions_num (optional, any, None)
      Total Data Sessions


    port_out_of_range (optional, any, None)
      Drop Data Port out of range



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


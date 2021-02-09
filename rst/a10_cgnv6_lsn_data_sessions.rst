.. _a10_cgnv6_lsn_data_sessions_module:


a10_cgnv6_lsn_data_sessions -- Configures A10 cgnv6.lsn.data-sessions
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

To clear lsn data sessions by user or NAT resource






Parameters
----------

  oper (False, any, None)
    Field oper


    status (optional, any, None)
      Field status


    nat_addr_start (optional, any, None)
      Field nat_addr_start


    inside_addr (optional, any, None)
      Field inside_addr


    nat_addr (optional, any, None)
      Field nat_addr


    inside_addr_start (optional, any, None)
      Field inside_addr_start


    inside_addr_end (optional, any, None)
      Field inside_addr_end


    nat_port (optional, any, None)
      Field nat_port


    inside_port (optional, any, None)
      Field inside_port


    nat_addr_end (optional, any, None)
      Field nat_addr_end



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


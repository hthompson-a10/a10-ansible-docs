.. _a10_slb_reset_unknown_conn_module:


a10_slb_reset_unknown_conn -- Configures A10 slb.reset-unknown-conn
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field reset_unknown_conn






Parameters
----------

  oper (False, any, None)
    Field oper


    unknown_conn_rate_limit (optional, any, None)
      Field unknown_conn_rate_limit


    unknown_conn_rate_limit_drop (optional, any, None)
      Field unknown_conn_rate_limit_drop


    unknown_conn_current_rate (optional, any, None)
      Field unknown_conn_current_rate



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


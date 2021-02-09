.. _a10_gslb_protocol_module:


a10_gslb_protocol -- Configures A10 gslb.protocol
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify GSLB Message Protocol parameters






Parameters
----------

  oper (False, any, None)
    Field oper


    session_list (optional, any, None)
      Field session_list



  auto_detect (False, any, None)
    Automatically detect SLB Config


  ansible_username (True, any, None)
    Username for AXAPI authentication


  status_interval (False, any, None)
    Specify GSLB Message Protocol update period (The GSLB Protocol update interval (seconds), default is 30)


  ping_site (False, any, None)
    name of site or ip address to ping


  use_mgmt_port (False, any, None)
    Use management port for connections in Shared Partition


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  use_mgmt_port_for_all_partitions (False, any, None)
    Use management port for connections in all L3v Partitions


  uuid (False, any, None)
    uuid of the object


  msg_format_acos_2x (False, any, None)
    Run GSLB Protocol in compatible mode with a ACOS 2.x GSLB peer


  state (True, any, None)
    State of the object to be created.


  enable_list (False, any, None)
    Field enable_list


    ntype (optional, any, None)
      'controller'= Enable/Disable GSLB protocol as GSLB controller; 'device'= Enable/Disable GSLB protocol as site device;


    uuid (optional, any, None)
      uuid of the object



  limit (False, any, None)
    Field limit


    message (optional, any, None)
      Amount of Messages, default is 10000 (Number)


    uuid (optional, any, None)
      uuid of the object


    ardt_session (optional, any, None)
      Sessions of Active RDT, default is 32768 (Number)


    ardt_query (optional, any, None)
      Query Messages of Active RDT, default is 200 (Number)


    ardt_response (optional, any, None)
      Response Messages of Active RDT, default is 1000 (Number)


    conn_response (optional, any, None)
      Response Messages of Connection Load, default is no limit (Number)


    response (optional, any, None)
      Amount of Response Messages, default is 3600 (Number)



  ansible_password (True, any, None)
    Password for AXAPI authentication









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


.. _a10_gslb_protocol_limit_module:


a10_gslb_protocol_limit -- Configures A10 gslb.protocol.limit
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Specify limit for GSLB Message Protocol






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ardt_session (False, any, None)
    Sessions of Active RDT, default is 32768 (Number)


  ardt_response (False, any, None)
    Response Messages of Active RDT, default is 1000 (Number)


  conn_response (False, any, None)
    Response Messages of Connection Load, default is no limit (Number)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ardt_query (False, any, None)
    Query Messages of Active RDT, default is 200 (Number)


  message (False, any, None)
    Amount of Messages, default is 10000 (Number)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  response (False, any, None)
    Amount of Response Messages, default is 3600 (Number)









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


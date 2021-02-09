.. _a10_snmp_server_view_module:


a10_snmp_server_view -- Configures A10 snmp-server.view
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Defines named 'view' - a subset of the overall OID tree






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  oid (True, any, None)
    MIB view family name or oid


  uuid (False, any, None)
    uuid of the object


  viewname (True, any, None)
    Name of the view


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ntype (False, any, None)
    'included'= MIB family is included in the view; 'excluded'= MIB family is excluded from the view;


  mask (False, any, None)
    Hex octets, separated by '.', mask of oid


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


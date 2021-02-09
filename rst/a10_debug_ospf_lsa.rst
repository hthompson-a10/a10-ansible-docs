.. _a10_debug_ospf_lsa_module:


a10_debug_ospf_lsa -- Configures A10 debug.ospf.lsa
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

OSPFv3 Link State Advertisement






Parameters
----------

  gererate (False, any, None)
    LSA Generation


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  flooding (False, any, None)
    LSA Flooding


  maxage (False, any, None)
    LSA MaxAge processing


  refresh (False, any, None)
    LSA Refreshment


  state (True, any, None)
    State of the object to be created.


  install (False, any, None)
    LSA Installation


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


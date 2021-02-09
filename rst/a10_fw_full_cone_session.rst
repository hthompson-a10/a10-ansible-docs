.. _a10_fw_full_cone_session_module:


a10_fw_full_cone_session -- Configures A10 fw.full-cone-session
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Full Cone Sessions






Parameters
----------

  oper (False, any, None)
    Field oper


    session_list (optional, any, None)
      Field session_list


    ipv6_addr (optional, any, None)
      Field ipv6_addr


    total (optional, any, None)
      Field total


    ipv4_addr (optional, any, None)
      Field ipv4_addr



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


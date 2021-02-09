.. _a10_vrrp_a_vrid_lead_module:


a10_vrrp_a_vrid_lead -- Configures A10 vrrp-a.vrid-lead
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Define a vrid-lead






Parameters
----------

  vrid_lead_str (True, any, None)
    VRRP-A VRID leader name


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  partition (False, any, None)
    Field partition


    partition (optional, any, None)
      Partition name


    shared_cfg (optional, any, None)
      Field shared_cfg


    name_cfg (optional, any, None)
      Field name_cfg



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


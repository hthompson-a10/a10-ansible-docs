.. _a10_fw_active_rule_set_module:


a10_fw_active_rule_set -- Configures A10 fw.active-rule-set
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Active firewall policy






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (False, any, None)
    Rule set name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  session_aging (False, any, None)
    Session Aging Template


  override_nat_aging (False, any, None)
    Override NAT idle-timeout


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


  uuid (False, any, None)
    uuid of the object









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


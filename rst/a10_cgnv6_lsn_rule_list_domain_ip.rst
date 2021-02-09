.. _a10_cgnv6_lsn_rule_list_domain_ip_module:


a10_cgnv6_lsn_rule_list_domain_ip -- Configures A10 cgnv6.lsn.rule.list.domain-ip
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Domain IP for LSN Rule-List






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'placeholder'= placeholder;



  oper (False, any, None)
    Field oper


    ip_list (optional, any, None)
      Field ip_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  lsn_rule_list_name (optional, any, None)
    Key to identify parent object


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


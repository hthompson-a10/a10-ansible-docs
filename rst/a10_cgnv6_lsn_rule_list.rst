.. _a10_cgnv6_lsn_rule_list_module:


a10_cgnv6_lsn_rule_list -- Configures A10 cgnv6.lsn-rule-list
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure LSN Rule-List






Parameters
----------

  domain_name_list (False, any, None)
    Field domain_name_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    name_domain (optional, any, None)
      Configure a Specific Rule-Set (Domain Name)


    user_tag (optional, any, None)
      Customized tag


    rule_cfg (optional, any, None)
      Field rule_cfg


    uuid (optional, any, None)
      uuid of the object



  ansible_username (True, any, None)
    Username for AXAPI authentication


  domain_ip (False, any, None)
    Field domain_ip


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  domain_list_name_list (False, any, None)
    Field domain_list_name_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    name_domain_list (optional, any, None)
      Configure a Specific Rule-Set (Domain List Name)


    user_tag (optional, any, None)
      Customized tag


    rule_cfg (optional, any, None)
      Field rule_cfg


    uuid (optional, any, None)
      uuid of the object



  name (True, any, None)
    LSN Rule-List Name


  default (False, any, None)
    Field default


    sampling_enable (optional, any, None)
      Field sampling_enable


    rule_cfg (optional, any, None)
      Field rule_cfg


    uuid (optional, any, None)
      uuid of the object



  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


  ip_list (False, any, None)
    Field ip_list


    sampling_enable (optional, any, None)
      Field sampling_enable


    ipv4_addr (optional, any, None)
      Configure a Specific Rule-Set (IP Network Address)


    user_tag (optional, any, None)
      Customized tag


    rule_cfg (optional, any, None)
      Field rule_cfg


    uuid (optional, any, None)
      uuid of the object



  http_match_domain_name (False, any, None)
    Enable match domain name in http request


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


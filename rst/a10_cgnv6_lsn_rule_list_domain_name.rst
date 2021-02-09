.. _a10_cgnv6_lsn_rule_list_domain_name_module:


a10_cgnv6_lsn_rule_list_domain_name -- Configures A10 cgnv6.lsn.rule.list.domain-name
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure a Specific Rule-Set (Domain Name)






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'placeholder'= placeholder;



  oper (False, any, None)
    Field oper


    rule_list (optional, any, None)
      Field rule_list


    name_domain (optional, any, None)
      Configure a Specific Rule-Set (Domain Name)


    rule_count (optional, any, None)
      Field rule_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    name_domain (optional, any, None)
      Configure a Specific Rule-Set (Domain Name)



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  name_domain (True, any, None)
    Configure a Specific Rule-Set (Domain Name)


  lsn_rule_list_name (optional, any, None)
    Key to identify parent object


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  rule_cfg (False, any, None)
    Field rule_cfg


    proto (optional, any, None)
      'tcp'= TCP L4 Protocol; 'udp'= UDP L4 Protocol; 'icmp'= ICMP L4 Protocol; 'others'= Other L4 Protocol; 'dscp'= Match dscp value;


    udp_cfg (optional, any, None)
      Field udp_cfg


    icmp_others_cfg (optional, any, None)
      Field icmp_others_cfg


    dscp_cfg (optional, any, None)
      Field dscp_cfg


    tcp_cfg (optional, any, None)
      Field tcp_cfg



  user_tag (False, any, None)
    Customized tag









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


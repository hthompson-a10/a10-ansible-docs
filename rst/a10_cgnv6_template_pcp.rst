.. _a10_cgnv6_template_pcp_module:


a10_cgnv6_template_pcp -- Configures A10 cgnv6.template.pcp
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Port Control Protocol Template






Parameters
----------

  map (False, any, None)
    PCP MAP Opcode (default is enabled)


  check_client_nonce (False, any, None)
    To validate NONCE value in PCP request (default= disabled)


  source_ipv6 (False, any, None)
    Specify source IPv6 address for IPv6 ANNOUNCE message


  ansible_username (True, any, None)
    Username for AXAPI authentication


  allow_third_party_from_lan (False, any, None)
    Allow third party request coming from LAN (default is disabled)


  minimum (False, any, None)
    To set minimum lifetime of PCP mappings (default 2 minutes)


  peer (False, any, None)
    PCP PEER Opcode (default is enabled)


  disable_map_filter (False, any, None)
    To disable processing of FILTER options in MAP request


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    PCP Template name


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_password (True, any, None)
    Password for AXAPI authentication


  source_ip (False, any, None)
    Specify source IP address for IPv4 ANNOUNCE message


  maximum (False, any, None)
    To set maximum lifetime of PCP mappings (default 1440 minutes)


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  pcp_server_port (False, any, None)
    PCP server listening port (default 5351) (PCP UDP destination port)


  announce (False, any, None)
    PCP ANNOUNCE Opcode (default is enabled)


  allow_third_party_from_wan (False, any, None)
    Allow third party request coming from WAN (default is disabled)


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


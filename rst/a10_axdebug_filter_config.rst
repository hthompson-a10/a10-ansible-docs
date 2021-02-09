.. _a10_axdebug_filter_config_module:


a10_axdebug_filter_config -- Configures A10 axdebug.filter-config
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Global debug filter






Parameters
----------

  ipv6_address (False, any, None)
    ipv6 address


  port_num_max (False, any, None)
    max port number


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip (False, any, None)
    IP


  offset (False, any, None)
    byte offset


  number (True, any, None)
    Specify filter id


  max_hex (False, any, None)
     max value


  ipv4_netmask (False, any, None)
    IP subnet mask


  port (False, any, None)
    port configurations


  comp_hex (False, any, None)
    value to compare


  src_port (False, any, None)
    src port number


  uuid (False, any, None)
    uuid of the object


  proto (False, any, None)
    ip protocol number


  src_mac_addr (False, any, None)
    src mac address


  dst (False, any, None)
    Destination


  proto_val (False, any, None)
    'icmp'= icmp; 'icmpv6'= icmpv6; 'tcp'= tcp; 'udp'= udp;


  hex (False, any, None)
    Define hex value


  dst_mac_addr (False, any, None)
    dest mac address


  src_ip (False, any, None)
    src IP


  state (True, any, None)
    State of the object to be created.


  exit (False, any, None)
    Exit from axdebug mode


  ipv6 (False, any, None)
    IPV6


  min_hex (False, any, None)
     min value


  src_mac (False, any, None)
    src mac address


  mac_addr (False, any, None)
    mac address


  dst_mac (False, any, None)
    dest mac address


  dst_port_num (False, any, None)
    dest Port number


  integer_min (False, any, None)
    min value


  ipv4_address (False, any, None)
    ip address


  mac (False, any, None)
    mac address


  WORD1 (False, any, None)
    WORD min value


  WORD0 (False, any, None)
    WORD0 to compare


  WORD2 (False, any, None)
    WORD max value


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  integer (False, any, None)
    Define decimal value


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  dst_ipv4_address (False, any, None)
    dest ip address


  src (False, any, None)
    Src


  ansible_port (True, any, None)
    Port for AXAPI authentication


  word (False, any, None)
    Define hex value


  integer_max (False, any, None)
    max value


  dst_ip (False, any, None)
    dest IP


  oper_range (False, any, None)
    'gt'= greater than; 'gte'= greater than or equal to; 'se'= smaller than or equal to; 'st'= smaller than; 'eq'= equal to; 'range'= select a range;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  prot_num (False, any, None)
    protocol number


  port_num_min (False, any, None)
    min port number


  src_ipv4_address (False, any, None)
    src ip address


  length (False, any, None)
    byte length


  l3_proto (False, any, None)
    'arp'= arp; 'neighbor'= neighbor;


  dst_port (False, any, None)
    dest port number


  integer_comp (False, any, None)
    value to compare


  src_port_num (False, any, None)
    src Port number


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


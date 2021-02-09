.. _a10_axdebug_module:


a10_axdebug -- Configures A10 axdebug
=====================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Packet Trace Options






Parameters
----------

  outgoing (False, any, None)
    Outgoing interface (For all ports, don't specify port number.)


  out_port_num (False, any, None)
    Port Numbers separated by commas(,) and hyphens(-) without spaces. ex= 4,5,10-30, or separated by spaces and double-quoted(')


  ansible_username (True, any, None)
    Username for AXAPI authentication


  save_config (False, any, None)
    Field save_config


    default (optional, any, None)
      save to default config file


    config_file (optional, any, None)
      config file name



  apply_config (False, any, None)
    Field apply_config


    config_file (optional, any, None)
      config file name



  sess_filter_dis (False, any, None)
    Disable session based filter


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  count (False, any, None)
    Maximum packets to capture per cpu. Default is 3000. (Maximum packets to capture. For umlimited, specify 0)


  capture (False, any, None)
    Field capture


    current_slot (optional, any, None)
      Only for current-slot of chassis


    save (optional, any, None)
      Save packets into file (Specify filename to save packets)


    brief (optional, any, None)
      Print basic packet information


    detail (optional, any, None)
      Include packet payload



  ansible_port (True, any, None)
    Port for AXAPI authentication


  incoming (False, any, None)
    Incoming interface. (For all ports, don't specify port number.)


  uuid (False, any, None)
    uuid of the object


  inc_port_num (False, any, None)
    Port Numbers separated by commas(,) and hyphens(-) without spaces. ex= 4,5,10-30, or separated by spaces and double-quoted(')


  filter_config_list (False, any, None)
    Field filter_config_list


    ipv6_address (optional, any, None)
      ipv6 address


    port_num_max (optional, any, None)
      max port number


    proto_val (optional, any, None)
      'icmp'= icmp; 'icmpv6'= icmpv6; 'tcp'= tcp; 'udp'= udp;


    ip (optional, any, None)
      IP


    offset (optional, any, None)
      byte offset


    number (optional, any, None)
      Specify filter id


    max_hex (optional, any, None)
       max value


    ipv4_netmask (optional, any, None)
      IP subnet mask


    dst_mac_addr (optional, any, None)
      dest mac address


    comp_hex (optional, any, None)
      value to compare


    src_port (optional, any, None)
      src port number


    uuid (optional, any, None)
      uuid of the object


    proto (optional, any, None)
      ip protocol number


    src_mac_addr (optional, any, None)
      src mac address


    dst (optional, any, None)
      Destination


    hex (optional, any, None)
      Define hex value


    port (optional, any, None)
      port configurations


    src_ip (optional, any, None)
      src IP


    exit (optional, any, None)
      Exit from axdebug mode


    ipv6 (optional, any, None)
      IPV6


    src_mac (optional, any, None)
      src mac address


    dst_port (optional, any, None)
      dest port number


    dst_mac (optional, any, None)
      dest mac address


    dst_port_num (optional, any, None)
      dest Port number


    integer_min (optional, any, None)
      min value


    ipv4_address (optional, any, None)
      ip address


    mac (optional, any, None)
      mac address


    WORD1 (optional, any, None)
      WORD min value


    WORD0 (optional, any, None)
      WORD0 to compare


    WORD2 (optional, any, None)
      WORD max value


    integer (optional, any, None)
      Define decimal value


    min_hex (optional, any, None)
       min value


    dst_ipv4_address (optional, any, None)
      dest ip address


    src (optional, any, None)
      Src


    word (optional, any, None)
      Define hex value


    integer_max (optional, any, None)
      max value


    dst_ip (optional, any, None)
      dest IP


    oper_range (optional, any, None)
      'gt'= greater than; 'gte'= greater than or equal to; 'se'= smaller than or equal to; 'st'= smaller than; 'eq'= equal to; 'range'= select a range;


    prot_num (optional, any, None)
      protocol number


    port_num_min (optional, any, None)
      min port number


    src_ipv4_address (optional, any, None)
      src ip address


    length (optional, any, None)
      byte length


    l3_proto (optional, any, None)
      'arp'= arp; 'neighbor'= neighbor;


    mac_addr (optional, any, None)
      mac address


    integer_comp (optional, any, None)
      value to compare


    src_port_num (optional, any, None)
      src Port number


    user_tag (optional, any, None)
      Customized tag



  length (False, any, None)
    Packet length to capture


  maxfile (False, any, None)
    Maximum number of debug packet files. Default is 100


  state (True, any, None)
    State of the object to be created.


  exit (False, any, None)
    Field exit


    stop_capture (optional, any, None)
      stop capture traffic



  timeout (False, any, None)
    Maximum number of minutes for a capture. Default is 5 minutes. For unlimited, specify 0


  ansible_password (True, any, None)
    Password for AXAPI authentication


  delete (False, any, None)
    Field delete


    config_file (optional, any, None)
      Delete AXDebug config file (Specify target filename to change)


    capture_file (optional, any, None)
      Delete a capture file (Specify target filename to change)










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


.. _a10_cgnv6_template_logging_module:


a10_cgnv6_template_logging -- Configures A10 cgnv6.template.logging
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Logging Template






Parameters
----------

  disable_log_by_destination (False, any, None)
    Field disable_log_by_destination


    ip_list (optional, any, None)
      Field ip_list


    ip6_list (optional, any, None)
      Field ip6_list


    others (optional, any, None)
      Disable logging for other L4 protocols


    tcp_list (optional, any, None)
      Field tcp_list


    icmp (optional, any, None)
      Disable logging for icmp traffic


    udp_list (optional, any, None)
      Field udp_list


    uuid (optional, any, None)
      uuid of the object



  ansible_username (True, any, None)
    Username for AXAPI authentication


  include_radius_attribute (False, any, None)
    Field include_radius_attribute


    insert_if_not_existing (optional, any, None)
      Configure what string is to be inserted for custom RADIUS attributes


    zero_in_custom_attr (optional, any, None)
      Insert 0000 for standard and custom attributes in log string


    framed_ipv6_prefix (optional, any, None)
      Include radius attributes for the prefix


    prefix_length (optional, any, None)
      '32'= Prefix length 32; '48'= Prefix length 48; '64'= Prefix length 64; '80'= Prefix length 80; '96'= Prefix length 96; '112'= Prefix length 112;


    attr_cfg (optional, any, None)
      Field attr_cfg


    no_quote (optional, any, None)
      No quotation marks for RADIUS attributes in logs



  include_destination (False, any, None)
    Include the destination IP and port in logs


  resolution (False, any, None)
    'seconds'= Logging timestamp resolution in seconds (default); '10-milliseconds'= Logging timestamp resolution in 10s of milli-seconds;


  service_group (False, any, None)
    Set NAT logging service-group


  severity (False, any, None)
    Field severity


    severity_val (optional, any, None)
      Logging severity level


    severity_string (optional, any, None)
      'emergency'= 0= Emergency; 'alert'= 1= Alert; 'critical'= 2= Critical; 'error'= 3= Error; 'warning'= 4= Warning; 'notice'= 5= Notice; 'informational'= 6= Informational; 'debug'= 7= Debug;



  batched_logging_disable (False, any, None)
    Disable multiple logs per packet


  facility (False, any, None)
    'kernel'= 0= Kernel; 'user'= 1= User-level; 'mail'= 2= Mail; 'daemon'= 3= System daemons; 'security-authorization'= 4= Security/authorization; 'syslog'= 5= Syslog internal; 'line-printer'= 6= Line printer; 'news'= 7= Network news; 'uucp'= 8= UUCP subsystem; 'cron'= 9= Time-related; 'security-authorization- private'= 10= Private security/authorization; 'ftp'= 11= FTP; 'ntp'= 12= NTP; 'audit'= 13= Audit; 'alert'= 14= Alert; 'clock'= 15= Clock-related; 'local0'= 16= Local use 0; 'local1'= 17= Local use 1; 'local2'= 18= Local use 2; 'local3'= 19= Local use 3; 'local4'= 20= Local use 4; 'local5'= 21= Local use 5; 'local6'= 22= Local use 6; 'local7'= 23= Local use 7;


  include_port_block_account (False, any, None)
    include bytes accounting information in port-batch-v2 port-mapping and fixed- nat user-ports messages


  custom (False, any, None)
    Field custom


    custom_message (optional, any, None)
      Field custom_message


    custom_header (optional, any, None)
      'use-syslog-header'= Use syslog header as custom log header;


    custom_time_stamp_format (optional, any, None)
      Customize the time stamp format (Customize the time-stamp format. Default=%Y%m%d%H%M%S)



  state (True, any, None)
    State of the object to be created.


  shared (False, any, None)
    Service group is in shared patition


  source_address (False, any, None)
    Field source_address


    ip (optional, any, None)
      Specify source IP address


    uuid (optional, any, None)
      uuid of the object


    ipv6 (optional, any, None)
      Specify source IPv6 address



  log_receiver (False, any, None)
    Field log_receiver


    secret_string (optional, any, None)
      The RADIUS server's secret


    radius (optional, any, None)
      Use RADIUS server for NAT logging


    encrypted (optional, any, None)
      Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)



  format (False, any, None)
    'binary'= Binary logging format; 'compact'= Compact ASCII logging format (Hex format with compact representation); 'custom'= Arbitrary custom logging format; 'default'= Default A10 logging format (ASCII); 'rfc5424'= RFC5424 compliant logging format; 'cef'= Common Event Format for logging;


  include_inside_user_mac (False, any, None)
    Include the inside user MAC address in logs


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  log (False, any, None)
    Field log


    map_dhcpv6 (optional, any, None)
      Field map_dhcpv6


    port_overloading (optional, any, None)
      Force logging of all port-overloading sessions


    sessions (optional, any, None)
      Log all data sessions created using NAT


    user_data (optional, any, None)
      Log LSN Subscriber Information


    port_mappings (optional, any, None)
      'creation'= Log only creation of NAT mappings; 'disable'= Disable Log creation and deletion of NAT mappings; 'both'= Log creation and deletion of NAT mappings;


    http_requests (optional, any, None)
      'host'= Log the HTTP Host Header; 'url'= Log the HTTP Request URL;


    fixed_nat (optional, any, None)
      Field fixed_nat


    merged_style (optional, any, None)
      Merge creation and deletion of session logs to one



  include_session_byte_count (False, any, None)
    include byte count in session deletion logs


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    Logging template name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  rule (False, any, None)
    Field rule


    rule_http_requests (optional, any, None)
      Field rule_http_requests


    interim_update_interval (optional, any, None)
      Log interim update of NAT mappings (Interim update interval in minutes(Interval is floored to a multiple of 5))



  include_partition_name (False, any, None)
    Include partition name in logging events


  include_http (False, any, None)
    Field include_http


    file_extension (optional, any, None)
      HTTP file extension


    request_number (optional, any, None)
      HTTP Request Number


    method (optional, any, None)
      Log the HTTP Request Method


    header_cfg (optional, any, None)
      Field header_cfg


    l4_session_info (optional, any, None)
      Log the L4 session information of the HTTP request



  source_port (False, any, None)
    Field source_port


    source_port_num (optional, any, None)
      Set source port for sending NAT syslogs (default= 514)


    any (optional, any, None)
      Use any source port



  rfc_custom (False, any, None)
    Field rfc_custom


    header (optional, any, None)
      Field header


    message (optional, any, None)
      Field message



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


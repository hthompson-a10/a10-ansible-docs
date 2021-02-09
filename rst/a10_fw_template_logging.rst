.. _a10_fw_template_logging_module:


a10_fw_template_logging -- Configures A10 fw.template.logging
=============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Logging Template






Parameters
----------

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



  format (False, any, None)
    'ascii'= A10 Text logging format (ASCII); 'cef'= Common Event Format for logging (default);


  resolution (False, any, None)
    'seconds'= Logging timestamp resolution in seconds (default); '10-milliseconds'= Logging timestamp resolution in 10s of milli-seconds;


  include_dest_fqdn (False, any, None)
    Include destination FQDN string


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  merged_style (False, any, None)
    Merge creation and deletion of session logs to one


  log (False, any, None)
    Field log


    http_requests (optional, any, None)
      'host'= Log the HTTP Host Header; 'url'= Log the HTTP Request URL;



  service_group (False, any, None)
    Bind a Service Group to the logging template (Service Group Name)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  severity (False, any, None)
    'emergency'= 0= Emergency; 'alert'= 1= Alert; 'critical'= 2= Critical; 'error'= 3= Error; 'warning'= 4= Warning; 'notice'= 5= Notice; 'informational'= 6= Informational; 'debug'= 7= Debug;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  facility (False, any, None)
    'kernel'= 0= Kernel; 'user'= 1= User-level; 'mail'= 2= Mail; 'daemon'= 3= System daemons; 'security-authorization'= 4= Security/authorization; 'syslog'= 5= Syslog internal; 'line-printer'= 6= Line printer; 'news'= 7= Network news; 'uucp'= 8= UUCP subsystem; 'cron'= 9= Time-related; 'security-authorization- private'= 10= Private security/authorization; 'ftp'= 11= FTP; 'ntp'= 12= NTP; 'audit'= 13= Audit; 'alert'= 14= Alert; 'clock'= 15= Clock-related; 'local0'= 16= Local use 0; 'local1'= 17= Local use 1; 'local2'= 18= Local use 2; 'local3'= 19= Local use 3; 'local4'= 20= Local use 4; 'local5'= 21= Local use 5; 'local6'= 22= Local use 6; 'local7'= 23= Local use 7;


  uuid (False, any, None)
    uuid of the object


  rule (False, any, None)
    Field rule


    rule_http_requests (optional, any, None)
      Field rule_http_requests



  name (True, any, None)
    Logging Template Name


  state (True, any, None)
    State of the object to be created.


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



  source_address (False, any, None)
    Field source_address


    ip (optional, any, None)
      Specify source IP address


    uuid (optional, any, None)
      uuid of the object


    ipv6 (optional, any, None)
      Specify source IPv6 address



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


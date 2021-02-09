.. _a10_ip_nat_template_logging_module:


a10_ip_nat_template_logging -- Configures A10 ip.nat.template.logging
=====================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

NAT Logging Template






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  severity (False, any, None)
    Field severity


    severity_val (optional, any, None)
      Logging severity level


    severity_string (optional, any, None)
      'emergency'= 0= Emergency; 'alert'= 1= Alert; 'critical'= 2= Critical; 'error'= 3= Error; 'warning'= 4= Warning; 'notice'= 5= Notice; 'informational'= 6= Informational; 'debug'= 7= Debug;



  include_destination (False, any, None)
    Include the destination IP and port in logs


  facility (False, any, None)
    'kernel'= 0= Kernel; 'user'= 1= User-level; 'mail'= 2= Mail; 'daemon'= 3= System daemons; 'security-authorization'= 4= Security/authorization; 'syslog'= 5= Syslog internal; 'line-printer'= 6= Line printer; 'news'= 7= Network news; 'uucp'= 8= UUCP subsystem; 'cron'= 9= Time-related; 'security-authorization- private'= 10= Private security/authorization; 'ftp'= 11= FTP; 'ntp'= 12= NTP; 'audit'= 13= Audit; 'alert'= 14= Alert; 'clock'= 15= Clock-related; 'local0'= 16= Local use 0; 'local1'= 17= Local use 1; 'local2'= 18= Local use 2; 'local3'= 19= Local use 3; 'local4'= 20= Local use 4; 'local5'= 21= Local use 5; 'local6'= 22= Local use 6; 'local7'= 23= Local use 7;


  log (False, any, None)
    Field log


    port_mappings (optional, any, None)
      'creation'= Log creation of NAT mappgins; 'disable'= Disable Log creation and deletion of NAT mappings;



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  service_group (False, any, None)
    Set NAT logging service-group


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    NAT logging template name


  user_tag (False, any, None)
    Customized tag


  include_rip_rport (False, any, None)
    Include the IP and port of real server in logs


  state (True, any, None)
    State of the object to be created.


  source_port (False, any, None)
    Field source_port


    source_port_num (optional, any, None)
      Set source port for sending NAT syslogs (default= 514)


    any (optional, any, None)
      Use any source port



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


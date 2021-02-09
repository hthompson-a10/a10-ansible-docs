.. _a10_health_monitor_module:


a10_health_monitor -- Configures A10 health.monitor
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Define the Health Monitor object






Parameters
----------

  sample_threshold (False, any, None)
    Number of samples in one epoch above which passive HC is enabled. If below or equal to the threshold, passive HC is disabled (Specify number of samples in one second (Default is 50). If the number of samples is 0, no action is taken)


  ansible_username (True, any, None)
    Username for AXAPI authentication


  status_code (False, any, None)
    'status-code-2xx'= Enable passive mode with 2xx http status code; 'status-code- non-5xx'= Enable passive mode with non-5xx http status code;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  strict_retry_on_server_err_resp (False, any, None)
    Require strictly retry


  threshold (False, any, None)
    Threshold percentage above which passive mode is enabled (Specify percentage (Default is 75%))


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  name (True, any, None)
    Monitor Name


  ansible_port (True, any, None)
    Port for AXAPI authentication


  retry (False, any, None)
    Specify the Healthcheck Retries (Retry Count (default 3))


  uuid (False, any, None)
    uuid of the object


  ssl_ciphers (False, any, None)
    Specify OpenSSL Cipher Suite name(s) for Health check (OpenSSL Cipher Suite(s) (Eg= AES128-SHA256), if the cipher is invalid, would give information at HM down reason)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  interval (False, any, None)
    Specify the Healthcheck Interval (Interval Value, in seconds (default 5))


  up_retry (False, any, None)
    Specify the Healthcheck Retries before declaring target up (Up-retry count (default 1))


  dsr_l2_strict (False, any, None)
    Enable strict L2dsr health-check


  override_ipv6 (False, any, None)
    Override implicitly inherited IPv6 address from target


  passive (False, any, None)
    Specify passive mode


  state (True, any, None)
    State of the object to be created.


  timeout (False, any, None)
    Specify the Healthcheck Timeout (Timeout Value, in seconds(default 5), Timeout should be less than or equal to interval)


  override_port (False, any, None)
    Override implicitly inherited port from target (Port number (1-65534))


  disable_after_down (False, any, None)
    Disable the target if health check failed


  passive_interval (False, any, None)
    Interval to do manual health checking while in passive mode (Specify value in seconds (Default is 10 s))


  user_tag (False, any, None)
    Customized tag


  method (False, any, None)
    Field method


    udp (optional, any, None)
      Field udp


    http (optional, any, None)
      Field http


    dns (optional, any, None)
      Field dns


    ntp (optional, any, None)
      Field ntp


    rtsp (optional, any, None)
      Field rtsp


    smtp (optional, any, None)
      Field smtp


    tcp (optional, any, None)
      Field tcp


    pop3 (optional, any, None)
      Field pop3


    radius (optional, any, None)
      Field radius


    external (optional, any, None)
      Field external


    compound (optional, any, None)
      Field compound


    icmp (optional, any, None)
      Field icmp


    imap (optional, any, None)
      Field imap


    ftp (optional, any, None)
      Field ftp


    sip (optional, any, None)
      Field sip


    database (optional, any, None)
      Field database


    snmp (optional, any, None)
      Field snmp


    kerberos_kdc (optional, any, None)
      Field kerberos_kdc


    tacplus (optional, any, None)
      Field tacplus


    https (optional, any, None)
      Field https


    ldap (optional, any, None)
      Field ldap



  override_ipv4 (False, any, None)
    Override implicitly inherited IPv4 address from target









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


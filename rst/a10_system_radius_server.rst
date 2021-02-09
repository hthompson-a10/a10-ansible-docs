.. _a10_system_radius_server_module:


a10_system_radius_server -- Configures A10 system.radius.server
===============================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure system as a RADIUS server






Parameters
----------

  oper (False, any, None)
    Field oper


    custom_attr_name (optional, any, None)
      Field custom_attr_name


    case_insensitive (optional, any, None)
      Field case_insensitive


    custom_attr_value (optional, any, None)
      Field custom_attr_value


    radius_table_entries_list (optional, any, None)
      Field radius_table_entries_list


    total_entries (optional, any, None)
      Field total_entries


    starts_with (optional, any, None)
      Field starts_with



  secret_string (False, any, None)
    The RADIUS secret


  ansible_username (True, any, None)
    Username for AXAPI authentication


  attribute (False, any, None)
    Field attribute


    prefix_number (optional, any, None)
      RADIUS attribute number


    custom_number (optional, any, None)
      RADIUS attribute number


    custom_vendor (optional, any, None)
      RADIUS vendor attribute information (RADIUS vendor ID)


    vendor (optional, any, None)
      RADIUS vendor attribute information (RADIUS vendor ID)


    name (optional, any, None)
      Customized attribute name


    number (optional, any, None)
      RADIUS attribute number


    value (optional, any, None)
      'hexadecimal'= Type of attribute value is hexadecimal;


    prefix_length (optional, any, None)
      '32'= Prefix length 32; '48'= Prefix length 48; '64'= Prefix length 64; '80'= Prefix length 80; '96'= Prefix length 96; '112'= Prefix length 112;


    prefix_vendor (optional, any, None)
      RADIUS vendor attribute information (RADIUS vendor ID)


    attribute_value (optional, any, None)
      'inside-ipv6-prefix'= Framed IPv6 Prefix; 'inside-ip'= Inside IP address; 'inside-ipv6'= Inside IPv6 address; 'imei'= International Mobile Equipment Identity (IMEI); 'imsi'= International Mobile Subscriber Identity (IMSI); 'msisdn'= Mobile Subscriber Integrated Services Digital Network-Number (MSISDN); 'custom1'= Customized attribute 1; 'custom2'= Customized attribute 2; 'custom3'= Customized attribute 3;



  disable_reply (False, any, None)
    Toggle option for RADIUS reply packet(Default= Accounting response will be sent)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  attribute_name (False, any, None)
    'msisdn'= Clear using MSISDN; 'imei'= Clear using IMEI; 'imsi'= Clear using IMSI; 'custom1'= Clear using CUSTOM1 attribute configured; 'custom2'= Clear using CUSTOM2 attribute configured; 'custom3'= Clear using CUSTOM3 attribute configured;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  accounting_start (False, any, None)
    'ignore'= Ignore; 'append-entry'= Append the AVPs to existing entry (default); 'replace-entry'= Replace the AVPs of existing entry;


  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'msisdn-received'= MSISDN Received; 'imei-received'= IMEI Received; 'imsi-received'= IMSI Received; 'custom-received'= Custom attribute Received; 'radius-request-received'= RADIUS Request Received; 'radius-request-dropped'= RADIUS Request Dropped (Malformed Packet); 'request-bad-secret-dropped'= RADIUS Request Bad Secret Dropped; 'request-no-key-vap-dropped'= RADIUS Request No Key Attribute Dropped; 'request-malformed-dropped'= RADIUS Request Malformed Dropped; 'request-ignored'= RADIUS Request Ignored; 'radius-table-full'= RADIUS Request Dropped (Table Full); 'secret-not-configured-dropped'= RADIUS Secret Not Configured Dropped; 'ha-standby-dropped'= HA Standby Dropped; 'ipv6-prefix- length-mismatch'= Framed IPV6 Prefix Length Mismatch; 'invalid-key'= Radius Request has Invalid Key Field; 'smp-created'= RADIUS SMP Created; 'smp- deleted'= RADIUS SMP Deleted; 'smp-mem-allocated'= RADIUS SMP Memory Allocated; 'smp-mem-alloc-failed'= RADIUS SMP Memory Allocation Failed; 'smp-mem-freed'= RADIUS SMP Memory Freed; 'smp-in-rml'= RADIUS SMP in RML; 'mem-allocated'= RADIUS Memory Allocated; 'mem-alloc-failed'= RADIUS Memory Allocation Failed; 'mem-freed'= RADIUS Memory Freed; 'ha-sync-create-sent'= HA Record Sync Create Sent; 'ha-sync-delete-sent'= HA Record Sync Delete Sent; 'ha-sync-create-recv'= HA Record Sync Create Received; 'ha-sync-delete-recv'= HA Record Sync Delete Received; 'acct-on-filters-full'= RADIUS Acct On Request Ignored(Filters Full); 'acct-on-dup-request'= Duplicate RADIUS Acct On Request; 'ip-mismatch-delete'= Radius Entry IP Mismatch Delete; 'ip-add-race-drop'= Radius Entry IP Add Race Drop; 'ha-sync-no-key-vap-dropped'= HA Record Sync No key dropped; 'inter-card- msg-fail-drop'= Inter-Card Message Fail Drop; 'radius-packets-redirected'= RADIUS packets redirected (SO); 'radius-packets-redirect-fail-dropped'= RADIUS packets dropped due to redirect failure (SO); 'radius-packets-process-local'= RADIUS packets processed locally without redirection (SO); 'radius-packets- dropped-not-lo'= RADIUS packets dropped dest not loopback (SO);



  accounting_stop (False, any, None)
    'ignore'= Ignore; 'delete-entry'= Delete the entry (default); 'delete-entry- and-sessions'= Delete the entry and data sessions associated(CGN only);


  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    secret_not_configured_dropped (optional, any, None)
      RADIUS Secret Not Configured Dropped


    radius_table_full (optional, any, None)
      RADIUS Request Dropped (Table Full)


    ha_standby_dropped (optional, any, None)
      HA Standby Dropped


    imsi_received (optional, any, None)
      IMSI Received


    ipv6_prefix_length_mismatch (optional, any, None)
      Framed IPV6 Prefix Length Mismatch


    custom_received (optional, any, None)
      Custom attribute Received


    request_no_key_vap_dropped (optional, any, None)
      RADIUS Request No Key Attribute Dropped


    request_bad_secret_dropped (optional, any, None)
      RADIUS Request Bad Secret Dropped


    invalid_key (optional, any, None)
      Radius Request has Invalid Key Field


    request_ignored (optional, any, None)
      RADIUS Request Ignored


    smp_created (optional, any, None)
      RADIUS SMP Created


    imei_received (optional, any, None)
      IMEI Received


    request_malformed_dropped (optional, any, None)
      RADIUS Request Malformed Dropped


    radius_request_dropped (optional, any, None)
      RADIUS Request Dropped (Malformed Packet)


    smp_deleted (optional, any, None)
      RADIUS SMP Deleted


    msisdn_received (optional, any, None)
      MSISDN Received


    radius_request_received (optional, any, None)
      RADIUS Request Received



  uuid (False, any, None)
    uuid of the object


  listen_port (False, any, None)
    Configure the listen port of RADIUS server (default 1813) (Port number)


  vrid (False, any, None)
    Join a VRRP-A failover group


  secret (False, any, None)
    Configure shared secret


  state (True, any, None)
    State of the object to be created.


  accounting_interim_update (False, any, None)
    'ignore'= Ignore (default); 'append-entry'= Append the AVPs to existing entry; 'replace-entry'= Replace the AVPs of existing entry;


  accounting_on (False, any, None)
    'ignore'= Ignore (default); 'delete-entries-using-attribute'= Delete entries matching attribute in RADIUS Table;


  encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  ansible_password (True, any, None)
    Password for AXAPI authentication


  remote (False, any, None)
    Field remote


    ip_list (optional, any, None)
      Field ip_list










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


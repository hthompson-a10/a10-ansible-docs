.. _a10_slb_health_check_details_module:


a10_slb_health_check_details -- Configures A10 slb.health-check-details
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Display Health Monitor Information for a given PIN and PID






Parameters
----------

  oper (False, any, None)
    Field oper


    expect_resp_code (optional, any, None)
      Field expect_resp_code


    attr_rpn (optional, any, None)
      Field attr_rpn


    starttls (optional, any, None)
      Field starttls


    attr_port (optional, any, None)
      Field attr_port


    ipaddr (optional, any, None)
      Field ipaddr


    attr_program (optional, any, None)
      Field attr_program


    community (optional, any, None)
      Field community


    dns_qtype (optional, any, None)
      Field dns_qtype


    base_dn (optional, any, None)
      Field base_dn


    health_state (optional, any, None)
      Field health_state


    query (optional, any, None)
      Field query


    tcp_only (optional, any, None)
      Field tcp_only


    expect_text (optional, any, None)
      Field expect_text


    rcv_integer (optional, any, None)
      Field rcv_integer


    send (optional, any, None)
      Field send


    secret (optional, any, None)
      Field secret


    sip_register (optional, any, None)
      Field sip_register


    db_row (optional, any, None)
      Field db_row


    resp_cont (optional, any, None)
      Field resp_cont


    attr_alias_addr (optional, any, None)
      Field attr_alias_addr


    http_req_sent (optional, any, None)
      Field http_req_sent


    mail_from (optional, any, None)
      Field mail_from


    rcpt_to (optional, any, None)
      Field rcpt_to


    db_name (optional, any, None)
      Field db_name


    pname (optional, any, None)
      Field pname


    force_up (optional, any, None)
      Field force_up


    dns_recurse (optional, any, None)
      Field dns_recurse


    status_code_rcv (optional, any, None)
      Field status_code_rcv


    curr_tcp_rtt (optional, any, None)
      Field curr_tcp_rtt


    expect_text_regex (optional, any, None)
      Field expect_text_regex


    receive (optional, any, None)
      Field receive


    kerberos_kdc (optional, any, None)
      Field kerberos_kdc


    avg_tcp_rtt (optional, any, None)
      Field avg_tcp_rtt


    expect_resp_regex_code (optional, any, None)
      Field expect_resp_regex_code


    http_wait_resp (optional, any, None)
      Field http_wait_resp


    curr_rtt (optional, any, None)
      Field curr_rtt


    curr_interval (optional, any, None)
      Field curr_interval


    domain (optional, any, None)
      Field domain


    l4_errors (optional, any, None)
      Field l4_errors


    postdata (optional, any, None)
      Field postdata


    half_open (optional, any, None)
      Field half_open


    pass (optional, any, None)
      Field pass


    dns_expect (optional, any, None)
      Field dns_expect


    monitor_name (optional, any, None)
      Field monitor_name


    received_fail (optional, any, None)
      Field received_fail


    state_reason (optional, any, None)
      Field state_reason


    pin_id (optional, any, None)
      Field pin_id


    snmp_operation (optional, any, None)
      Field snmp_operation


    maintenance_code (optional, any, None)
      Field maintenance_code


    arguments (optional, any, None)
      Field arguments


    method (optional, any, None)
      Field method


    avg_rtt (optional, any, None)
      Field avg_rtt


    response_timeout (optional, any, None)
      Field response_timeout


    oid (optional, any, None)
      Field oid


    http_errors (optional, any, None)
      Field http_errors


    host (optional, any, None)
      Field host


    l4_conn_num (optional, any, None)
      Field l4_conn_num


    ldap_ssl (optional, any, None)
      Field ldap_ssl


    user (optional, any, None)
      Field user


    received_success (optional, any, None)
      Field received_success


    kerberos_realm (optional, any, None)
      Field kerberos_realm


    ldap_tls (optional, any, None)
      Field ldap_tls


    process_index (optional, any, None)
      Field process_index


    db_column (optional, any, None)
      Field db_column


    url (optional, any, None)
      Field url


    kerberos_port (optional, any, None)
      Field kerberos_port


    transport_proto (optional, any, None)
      Field transport_proto


    mac_addr (optional, any, None)
      Field mac_addr


    dns_expect_type (optional, any, None)
      Field dns_expect_type


    attr_type (optional, any, None)
      Field attr_type



  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication









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


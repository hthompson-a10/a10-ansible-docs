.. _a10_slb_pop3_proxy_module:


a10_slb_pop3_proxy -- Configures A10 slb.pop3-proxy
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure POP3 Proxy global






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'num'= Num; 'curr'= Current proxy conns; 'total'= Total proxy conns; 'svrsel_fail'= Server selection failure; 'no_route'= no route failure; 'snat_fail'= source nat failure; 'line_too_long'= line too long; 'line_mem_freed'= request line freed; 'invalid_start_line'= invalid start line; 'stls'= stls cmd; 'request_dont_care'= other cmd; 'unsupported_command'= Unsupported cmd; 'bad_sequence'= Bad Sequence; 'rsv_persist_conn_fail'= Serv Sel Persist fail; 'smp_v6_fail'= Serv Sel SMPv6 fail; 'smp_v4_fail'= Serv Sel SMPv4 fail; 'insert_tuple_fail'= Serv Sel insert tuple fail; 'cl_est_err'= Client EST state erro; 'ser_connecting_err'= Serv CTNG state error; 'server_response_err'= Serv RESP state error; 'cl_request_err'= Client RQ state error; 'request'= Total POP3 Request; 'control_to_ssl'= Control chn ssl;



  oper (False, any, None)
    Field oper


    l4_cpu_list (optional, any, None)
      Field l4_cpu_list


    cpu_count (optional, any, None)
      Field cpu_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    ser_connecting_err (optional, any, None)
      Serv CTNG state error


    svrsel_fail (optional, any, None)
      Server selection failure


    curr (optional, any, None)
      Current proxy conns


    cl_request_err (optional, any, None)
      Client RQ state error


    server_response_err (optional, any, None)
      Serv RESP state error


    smp_v6_fail (optional, any, None)
      Serv Sel SMPv6 fail


    smp_v4_fail (optional, any, None)
      Serv Sel SMPv4 fail


    snat_fail (optional, any, None)
      source nat failure


    no_route (optional, any, None)
      no route failure


    total (optional, any, None)
      Total proxy conns


    rsv_persist_conn_fail (optional, any, None)
      Serv Sel Persist fail


    control_to_ssl (optional, any, None)
      Control chn ssl


    request_dont_care (optional, any, None)
      other cmd


    cl_est_err (optional, any, None)
      Client EST state erro


    line_too_long (optional, any, None)
      line too long


    bad_sequence (optional, any, None)
      Bad Sequence


    request (optional, any, None)
      Total POP3 Request


    insert_tuple_fail (optional, any, None)
      Serv Sel insert tuple fail


    line_mem_freed (optional, any, None)
      request line freed


    unsupported_command (optional, any, None)
      Unsupported cmd


    num (optional, any, None)
      Num


    stls (optional, any, None)
      stls cmd


    invalid_start_line (optional, any, None)
      invalid start line



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


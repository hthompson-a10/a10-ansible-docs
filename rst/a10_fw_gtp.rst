.. _a10_fw_gtp_module:


a10_fw_gtp -- Configures A10 fw.gtp
===================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure GTP






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'create-session-request'= Create Session Request; 'create-session- response'= Create Session Response; 'path-management-message'= Path Management Message; 'delete-session-request'= Delete Session Request; 'delete-session- response'= Delete Session Response; 'reserved-field-set-drop'= Reserved field set drop; 'tunnel-id-flag-drop'= Tunnel ID Flag Incorrect; 'message-filtering- drop'= Message Filtering Drop; 'reserved-information-element-drop'= Resevered Information Element Field Drop; 'mandatory-information-element-drop'= Mandatory Information Element Field Drop; 'filter-list-drop'= APN IMSI Information Filtering Drop; 'invalid-teid-drop'= Invalid TEID Drop; 'out-of-state-drop'= Out Of State Drop; 'message-length-drop'= Message Length Exceeded; 'unsupported-message-type-v2'= GTP v2 message type is not supported; 'fast- conn-setup'= Fast Conn Setup Attempt; 'out-of-session-memory'= Out of Session Memory; 'no-fwd-route'= No Forward Route; 'no-rev-route'= NO Reverse Route; 'invalid-key'= Invalid TEID Field; 'create-session-request-retransmit'= Retransmitted Create Session Request; 'delete-session-request-retransmit'= Retransmitted Delete Session Request; 'response-cause-not-accepted'= Response Cause indicates Request not Accepted; 'invalid-imsi-len-drop'= Invalid IMSI Length Drop; 'invalid-apn-len-drop'= Invalid APN Length Drop; 'create-pdp- context-request-v1'= GTP v1 Create PDP Context Request; 'create-pdp-context- response-v1'= GTP v1 Create PDP Context Response; 'path-management-message-v1'= GTP v1 Path Management Message; 'reserved-field-set-drop-v1'= GTP v1 Reserved field set drop; 'message-filtering-drop-v1'= GTP v1 Message Filtering Drop; 'reserved-information-element-drop-v1'= GTP v1 Reserved Information Element Field Drop; 'mandatory-information-element-drop-v1'= GTP v1 Mandatory Information Element Field Drop; 'filter-list-drop-v1'= GTP v1 APN IMSI Information Filtering Drop; 'invalid-teid-drop-v1'= GTP v1 Invalid TEID Drop; 'message-length-drop-v1'= GTP v1 Message Length Exceeded; 'version-not- supported'= GTP version is not supported; 'unsupported-message-type-v1'= GTP v1 message type is not supported; 'delete-pdp-context-request-v1'= GTP v1 Delete Context PDP Request; 'delete-pdp-context-response-v1'= GTP v1 Delete Context PDP Response; 'create-pdp-context-request-v0'= GTP v0 Create PDP Context Request; 'create-pdp-context-response-v0'= GTP v0 Create PDP Context Response; 'delete-pdp-context-request-v0'= GTP v0 Delete Context PDP Request; 'delete- pdp-context-response-v0'= GTP v0 Delete Context PDP Response; 'path-management- message-v0'= GTP v0 Path Management Message; 'message-filtering-drop-v0'= GTP v0 Message Filtering Drop; 'unsupported-message-type-v0'= GTP v0 message type is not supported; 'invalid-flow-label-drop-v0'= GTP v0 Invalid flow label drop; 'invalid-tid-drop-v0'= GTP v0 Invalid tid drop; 'message-length-drop-v0'= GTP v0 Message Length Exceeded; 'mandatory-information-element-drop-v0'= GTP v0 Mandatory Information Element Field Drop; 'filter-list-drop-v0'= GTP v0 APN IMSI Information Filtering Drop; 'gtp-in-gtp-drop'= GTP in GTP Filtering Drop;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    invalid_imsi_len_drop (optional, any, None)
      Invalid IMSI Length Drop


    out_of_session_memory (optional, any, None)
      Out of Session Memory


    reserved_information_element_drop_v1 (optional, any, None)
      GTP v1 Reserved Information Element Field Drop


    mandatory_information_element_drop (optional, any, None)
      Mandatory Information Element Field Drop


    path_management_message_v0 (optional, any, None)
      GTP v0 Path Management Message


    path_management_message_v1 (optional, any, None)
      GTP v1 Path Management Message


    filter_list_drop (optional, any, None)
      APN IMSI Information Filtering Drop


    version_not_supported (optional, any, None)
      GTP version is not supported


    create_session_response (optional, any, None)
      Create Session Response


    mandatory_information_element_drop_v1 (optional, any, None)
      GTP v1 Mandatory Information Element Field Drop


    mandatory_information_element_drop_v0 (optional, any, None)
      GTP v0 Mandatory Information Element Field Drop


    delete_session_response (optional, any, None)
      Delete Session Response


    delete_session_request (optional, any, None)
      Delete Session Request


    invalid_key (optional, any, None)
      Invalid TEID Field


    out_of_state_drop (optional, any, None)
      Out Of State Drop


    create_pdp_context_request_v1 (optional, any, None)
      GTP v1 Create PDP Context Request


    create_pdp_context_request_v0 (optional, any, None)
      GTP v0 Create PDP Context Request


    message_length_drop_v1 (optional, any, None)
      GTP v1 Message Length Exceeded


    message_length_drop_v0 (optional, any, None)
      GTP v0 Message Length Exceeded


    message_filtering_drop (optional, any, None)
      Message Filtering Drop


    invalid_apn_len_drop (optional, any, None)
      Invalid APN Length Drop


    invalid_teid_drop_v1 (optional, any, None)
      GTP v1 Invalid TEID Drop


    invalid_teid_drop (optional, any, None)
      Invalid TEID Drop


    no_fwd_route (optional, any, None)
      No Forward Route


    create_pdp_context_response_v0 (optional, any, None)
      GTP v0 Create PDP Context Response


    create_pdp_context_response_v1 (optional, any, None)
      GTP v1 Create PDP Context Response


    delete_pdp_context_request_v0 (optional, any, None)
      GTP v0 Delete Context PDP Request


    message_length_drop (optional, any, None)
      Message Length Exceeded


    gtp_in_gtp_drop (optional, any, None)
      GTP in GTP Filtering Drop


    invalid_tid_drop_v0 (optional, any, None)
      GTP v0 Invalid tid drop


    create_session_request (optional, any, None)
      Create Session Request


    filter_list_drop_v1 (optional, any, None)
      GTP v1 APN IMSI Information Filtering Drop


    invalid_flow_label_drop_v0 (optional, any, None)
      GTP v0 Invalid flow label drop


    path_management_message (optional, any, None)
      Path Management Message


    no_rev_route (optional, any, None)
      NO Reverse Route


    reserved_field_set_drop (optional, any, None)
      Reserved field set drop


    delete_pdp_context_request_v1 (optional, any, None)
      GTP v1 Delete Context PDP Request


    response_cause_not_accepted (optional, any, None)
      Response Cause indicates Request not Accepted


    delete_session_request_retransmit (optional, any, None)
      Retransmitted Delete Session Request


    unsupported_message_type_v2 (optional, any, None)
      GTP v2 message type is not supported


    unsupported_message_type_v0 (optional, any, None)
      GTP v0 message type is not supported


    unsupported_message_type_v1 (optional, any, None)
      GTP v1 message type is not supported


    filter_list_drop_v0 (optional, any, None)
      GTP v0 APN IMSI Information Filtering Drop


    tunnel_id_flag_drop (optional, any, None)
      Tunnel ID Flag Incorrect


    create_session_request_retransmit (optional, any, None)
      Retransmitted Create Session Request


    reserved_field_set_drop_v1 (optional, any, None)
      GTP v1 Reserved field set drop


    delete_pdp_context_response_v1 (optional, any, None)
      GTP v1 Delete Context PDP Response


    delete_pdp_context_response_v0 (optional, any, None)
      GTP v0 Delete Context PDP Response


    fast_conn_setup (optional, any, None)
      Fast Conn Setup Attempt


    message_filtering_drop_v0 (optional, any, None)
      GTP v0 Message Filtering Drop


    message_filtering_drop_v1 (optional, any, None)
      GTP v1 Message Filtering Drop


    reserved_information_element_drop (optional, any, None)
      Resevered Information Element Field Drop



  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  gtp_value (False, any, None)
    'enable'= Enable GTP Inspection;


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


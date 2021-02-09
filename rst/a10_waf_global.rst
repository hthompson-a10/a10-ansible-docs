.. _a10_waf_global_module:


a10_waf_global -- Configures A10 waf.global
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

WAF global stats






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'total_req'= Total Requests; 'req_allowed'= Requests Allowed; 'req_denied'= Requests Denied; 'bot_check_succ'= Botnet Check Success; 'bot_check_fail'= Botnet Check Failure; 'form_consistency_succ'= Form Consistency Success; 'form_consistency_fail'= Form Consistency Failure; 'form_csrf_tag_succ'= Form CSRF tag Success; 'form_csrf_tag_fail'= Form CSRF tag Failure; 'url_check_succ'= URL Check Success; 'url_check_fail'= URL Check Failure; 'url_check_learn'= URL Check Learn; 'buf_ovf_url_len_fail'= Buffer Overflow - URL Length Failure; 'buf_ovf_cookie_len_fail'= Buffer Overflow - Cookie Length Failure; 'buf_ovf_hdrs_len_fail'= Buffer Overflow - Headers length Failure; 'buf_ovf_post_size_fail'= Buffer Overflow - Post size Failure; 'max_cookies_fail'= Max Cookies Failure; 'max_hdrs_fail'= Max Headers Failure; 'http_method_check_succ'= Http Method Check Success; 'http_method_check_fail'= Http Method Check Failure; 'http_check_succ'= Http Check Success; 'http_check_fail'= Http Check Failure; 'referer_check_succ'= Referer Check Success; 'referer_check_fail'= Referer Check Failure; 'referer_check_redirect'= Referer Check Redirect; 'uri_wlist_succ'= URI White List Success; 'uri_wlist_fail'= URI White List Failure; 'uri_blist_succ'= URI Black List Success; 'uri_blist_fail'= URI Black List Failure; 'post_form_check_succ'= Post Form Check Success; 'post_form_check_sanitize'= Post Form Check Sanitized; 'post_form_check_reject'= Post Form Check Rejected; 'ccn_mask_amex'= Credit Card Number Mask Amex; 'ccn_mask_diners'= Credit Card Number Mask Diners; 'ccn_mask_visa'= Credit Card Number Mask Visa; 'ccn_mask_mastercard'= Credit Card Number Mask Mastercard; 'ccn_mask_discover'= Credit Card Number Mask Discover; 'ccn_mask_jcb'= Credit Card Number Mask Jcb; 'ssn_mask'= Social Security Number Mask; 'pcre_mask'= PCRE Mask; 'cookie_encrypt_succ'= Cookie Encrypt Success; 'cookie_encrypt_fail'= Cookie Encrypt Failure; 'cookie_encrypt_limit_exceeded'= Cookie Encrypt Limit Exceeded; 'cookie_encrypt_skip_rcache'= Cookie Encrypt Skip RCache; 'cookie_decrypt_succ'= Cookie Decrypt Success; 'cookie_decrypt_fail'= Cookie Decrypt Failure; 'sqlia_chk_url_succ'= SQLIA Check URL Success; 'sqlia_chk_url_sanitize'= SQLIA Check URL Sanitized; 'sqlia_chk_url_reject'= SQLIA Check URL Rejected; 'sqlia_chk_post_succ'= SQLIA Check Post Success; 'sqlia_chk_post_sanitize'= SQLIA Check Post Sanitized; 'sqlia_chk_post_reject'= SQLIA Check Post Rejected; 'xss_chk_cookie_succ'= XSS Check Cookie Success; 'xss_chk_cookie_sanitize'= XSS Check Cookie Sanitized; 'xss_chk_cookie_reject'= XSS Check Cookie Rejected; 'xss_chk_url_succ'= XSS Check URL Success; 'xss_chk_url_sanitize'= XSS Check URL Sanitized; 'xss_chk_url_reject'= XSS Check URL Rejected; 'xss_chk_post_succ'= XSS Check Post Success; 'xss_chk_post_sanitize'= XSS Check Post Sanitized; 'xss_chk_post_reject'= XSS Check Post Rejected; 'resp_code_hidden'= Response Code Hidden; 'resp_hdrs_filtered'= Response Headers Filtered; 'learn_updates'= Learning Updates; 'num_drops'= Number Drops; 'num_resets'= Number Resets; 'form_non_ssl_reject'= Form Non SSL Rejected; 'form_non_post_reject'= Form Non Post Rejected; 'sess_check_none'= Session Check None; 'sess_check_succ'= Session Check Success; 'sess_check_fail'= Session Check Failure; 'soap_check_succ'= Soap Check Success; 'soap_check_failure'= Soap Check Failure; 'wsdl_fail'= WSDL Failure; 'wsdl_succ'= WSDL Success; 'xml_schema_fail'= XML Schema Failure; 'xml_schema_succ'= XML Schema Success; 'xml_sqlia_chk_fail'= XML Sqlia Check Failure; 'xml_sqlia_chk_succ'= XML Sqlia Check Success; 'xml_xss_chk_fail'= XML XSS Check Failure; 'xml_xss_chk_succ'= XML XSS Check Success; 'json_check_failure'= JSON Check Failure; 'json_check_succ'= JSON Check Success; 'xml_check_failure'= XML Check Failure; 'xml_check_succ'= XML Check Success; 'buf_ovf_cookie_value_len_fail'= Buffer Overflow - Cookie Value Length Failure; 'buf_ovf_cookies_len_fail'= Buffer Overflow - Cookies Length Failure; 'buf_ovf_hdr_name_len_fail'= Buffer Overflow - Header Name Length Failure; 'buf_ovf_hdr_value_len_fail'= Buffer Overflow - Header Value Length Failure; 'buf_ovf_max_data_parse_fail'= Buffer Overflow - Max Data Parse Failure; 'buf_ovf_line_len_fail'= Buffer Overflow - Line Length Failure; 'buf_ovf_parameter_name_len_fail'= Buffer Overflow - HTML Parameter Name Length Failure; 'buf_ovf_parameter_value_len_fail'= Buffer Overflow - HTML Parameter Value Length Failure; 'buf_ovf_parameter_total_len_fail'= Buffer Overflow - HTML Parameter Total Length Failure; 'buf_ovf_query_len_fail'= Buffer Overflow - Query Length Failure; 'max_entities_fail'= Max Entities Failure; 'max_parameters_fail'= Max Parameters Failure; 'buf_ovf_cookie_name_len_fail'= Buffer Overflow - Cookie Name Length Failure; 'xml_limit_attr'= XML Limit Attribue; 'xml_limit_attr_name_len'= XML Limit Name Length; 'xml_limit_attr_value_len'= XML Limit Value Length; 'xml_limit_cdata_len'= XML Limit CData Length; 'xml_limit_elem'= XML Limit Element; 'xml_limit_elem_child'= XML Limit Element Child; 'xml_limit_elem_depth'= XML Limit Element Depth; 'xml_limit_elem_name_len'= XML Limit Element Name Length; 'xml_limit_entity_exp'= XML Limit Entity Exp; 'xml_limit_entity_exp_depth'= XML Limit Entity Exp Depth; 'xml_limit_namespace'= XML Limit Namespace; 'xml_limit_namespace_uri_len'= XML Limit Namespace URI Length; 'json_limit_array_value_count'= JSON Limit Array Value Count; 'json_limit_depth'= JSON Limit Depth; 'json_limit_object_member_count'= JSON Limit Object Number Count; 'json_limit_string'= JSON Limit String; 'form_non_masked_password'= Form Non Masked Password; 'form_non_ssl_password'= Form Non SSL Password; 'form_password_autocomplete'= Form Password Autocomplete; 'redirect_wlist_succ'= Redirect Whitelist Success; 'redirect_wlist_fail'= Redirect Whitelist Failure; 'redirect_wlist_learn'= Redirect Whitelist Learn; 'form_set_no_cache'= Form Set No Cache; 'resp_denied'= Responses Denied; 'sessions_alloc'= Sessions allocated; 'sessions_freed'= Sessions freed; 'out_of_sessions'= Out of sessions; 'too_many_sessions'= Too many sessions consumed; 'called'= Threshold check count; 'permitted'= Honor threshold  count; 'brute_force_success'= Brute-force checks passed; 'brute_force_fail'= Brute- force checks failed; 'challenge_cookie_sent'= Cookie challenge sent; 'challenge_javascript_sent'= JavaScript challenge sent; 'challenge_captcha_sent'= Captcha challenge sent;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    redirect_wlist_fail (optional, any, None)
      Redirect Whitelist Failure


    cookie_encrypt_limit_exceeded (optional, any, None)
      Cookie Encrypt Limit Exceeded


    wsdl_succ (optional, any, None)
      WSDL Success


    sqlia_chk_url_succ (optional, any, None)
      SQLIA Check URL Success


    bot_check_succ (optional, any, None)
      Botnet Check Success


    cookie_encrypt_skip_rcache (optional, any, None)
      Cookie Encrypt Skip RCache


    redirect_wlist_learn (optional, any, None)
      Redirect Whitelist Learn


    xml_limit_elem_child (optional, any, None)
      XML Limit Element Child


    buf_ovf_parameter_value_len_fail (optional, any, None)
      Buffer Overflow - HTML Parameter Value Length Failure


    ccn_mask_visa (optional, any, None)
      Credit Card Number Mask Visa


    xss_chk_cookie_succ (optional, any, None)
      XSS Check Cookie Success


    buf_ovf_cookies_len_fail (optional, any, None)
      Buffer Overflow - Cookies Length Failure


    req_denied (optional, any, None)
      Requests Denied


    json_check_failure (optional, any, None)
      JSON Check Failure


    xss_chk_post_reject (optional, any, None)
      XSS Check Post Rejected


    xss_chk_url_reject (optional, any, None)
      XSS Check URL Rejected


    form_consistency_succ (optional, any, None)
      Form Consistency Success


    xml_limit_cdata_len (optional, any, None)
      XML Limit CData Length


    xml_check_failure (optional, any, None)
      XML Check Failure


    buf_ovf_hdrs_len_fail (optional, any, None)
      Buffer Overflow - Headers length Failure


    referer_check_succ (optional, any, None)
      Referer Check Success


    soap_check_succ (optional, any, None)
      Soap Check Success


    xss_chk_url_sanitize (optional, any, None)
      XSS Check URL Sanitized


    cookie_encrypt_succ (optional, any, None)
      Cookie Encrypt Success


    buf_ovf_parameter_total_len_fail (optional, any, None)
      Buffer Overflow - HTML Parameter Total Length Failure


    sqlia_chk_post_succ (optional, any, None)
      SQLIA Check Post Success


    max_cookies_fail (optional, any, None)
      Max Cookies Failure


    json_limit_array_value_count (optional, any, None)
      JSON Limit Array Value Count


    uri_wlist_succ (optional, any, None)
      URI White List Success


    json_check_succ (optional, any, None)
      JSON Check Success


    resp_code_hidden (optional, any, None)
      Response Code Hidden


    xml_sqlia_chk_fail (optional, any, None)
      XML Sqlia Check Failure


    xss_chk_post_succ (optional, any, None)
      XSS Check Post Success


    pcre_mask (optional, any, None)
      PCRE Mask


    form_consistency_fail (optional, any, None)
      Form Consistency Failure


    http_check_fail (optional, any, None)
      Http Check Failure


    url_check_succ (optional, any, None)
      URL Check Success


    sqlia_chk_url_reject (optional, any, None)
      SQLIA Check URL Rejected


    sqlia_chk_url_sanitize (optional, any, None)
      SQLIA Check URL Sanitized


    xss_chk_cookie_reject (optional, any, None)
      XSS Check Cookie Rejected


    brute_force_success (optional, any, None)
      Brute-force checks passed


    http_check_succ (optional, any, None)
      Http Check Success


    max_entities_fail (optional, any, None)
      Max Entities Failure


    http_method_check_fail (optional, any, None)
      Http Method Check Failure


    form_non_ssl_reject (optional, any, None)
      Form Non SSL Rejected


    xss_chk_post_sanitize (optional, any, None)
      XSS Check Post Sanitized


    form_set_no_cache (optional, any, None)
      Form Set No Cache


    xml_schema_succ (optional, any, None)
      XML Schema Success


    xml_limit_attr (optional, any, None)
      XML Limit Attribue


    xml_check_succ (optional, any, None)
      XML Check Success


    sess_check_none (optional, any, None)
      Session Check None


    xml_limit_namespace (optional, any, None)
      XML Limit Namespace


    wsdl_fail (optional, any, None)
      WSDL Failure


    post_form_check_succ (optional, any, None)
      Post Form Check Success


    buf_ovf_query_len_fail (optional, any, None)
      Buffer Overflow - Query Length Failure


    sqlia_chk_post_reject (optional, any, None)
      SQLIA Check Post Rejected


    form_password_autocomplete (optional, any, None)
      Form Password Autocomplete


    permitted (optional, any, None)
      Honor threshold  count


    xml_xss_chk_fail (optional, any, None)
      XML XSS Check Failure


    buf_ovf_url_len_fail (optional, any, None)
      Buffer Overflow - URL Length Failure


    buf_ovf_cookie_len_fail (optional, any, None)
      Buffer Overflow - Cookie Length Failure


    form_csrf_tag_succ (optional, any, None)
      Form CSRF tag Success


    xss_chk_cookie_sanitize (optional, any, None)
      XSS Check Cookie Sanitized


    sessions_alloc (optional, any, None)
      Sessions allocated


    xml_limit_entity_exp (optional, any, None)
      XML Limit Entity Exp


    ccn_mask_diners (optional, any, None)
      Credit Card Number Mask Diners


    sess_check_succ (optional, any, None)
      Session Check Success


    json_limit_depth (optional, any, None)
      JSON Limit Depth


    buf_ovf_cookie_name_len_fail (optional, any, None)
      Buffer Overflow - Cookie Name Length Failure


    learn_updates (optional, any, None)
      Learning Updates


    redirect_wlist_succ (optional, any, None)
      Redirect Whitelist Success


    challenge_javascript_sent (optional, any, None)
      JavaScript challenge sent


    req_allowed (optional, any, None)
      Requests Allowed


    json_limit_object_member_count (optional, any, None)
      JSON Limit Object Number Count


    bot_check_fail (optional, any, None)
      Botnet Check Failure


    uri_wlist_fail (optional, any, None)
      URI White List Failure


    uri_blist_fail (optional, any, None)
      URI Black List Failure


    referer_check_redirect (optional, any, None)
      Referer Check Redirect


    challenge_cookie_sent (optional, any, None)
      Cookie challenge sent


    sqlia_chk_post_sanitize (optional, any, None)
      SQLIA Check Post Sanitized


    ccn_mask_amex (optional, any, None)
      Credit Card Number Mask Amex


    num_drops (optional, any, None)
      Number Drops


    referer_check_fail (optional, any, None)
      Referer Check Failure


    post_form_check_sanitize (optional, any, None)
      Post Form Check Sanitized


    cookie_decrypt_succ (optional, any, None)
      Cookie Decrypt Success


    max_parameters_fail (optional, any, None)
      Max Parameters Failure


    url_check_fail (optional, any, None)
      URL Check Failure


    xml_schema_fail (optional, any, None)
      XML Schema Failure


    form_non_post_reject (optional, any, None)
      Form Non Post Rejected


    num_resets (optional, any, None)
      Number Resets


    xml_limit_entity_exp_depth (optional, any, None)
      XML Limit Entity Exp Depth


    form_non_masked_password (optional, any, None)
      Form Non Masked Password


    buf_ovf_line_len_fail (optional, any, None)
      Buffer Overflow - Line Length Failure


    ccn_mask_discover (optional, any, None)
      Credit Card Number Mask Discover


    ssn_mask (optional, any, None)
      Social Security Number Mask


    json_limit_string (optional, any, None)
      JSON Limit String


    resp_hdrs_filtered (optional, any, None)
      Response Headers Filtered


    called (optional, any, None)
      Threshold check count


    ccn_mask_mastercard (optional, any, None)
      Credit Card Number Mask Mastercard


    xml_sqlia_chk_succ (optional, any, None)
      XML Sqlia Check Success


    brute_force_fail (optional, any, None)
      Brute-force checks failed


    max_hdrs_fail (optional, any, None)
      Max Headers Failure


    xml_limit_attr_name_len (optional, any, None)
      XML Limit Name Length


    form_non_ssl_password (optional, any, None)
      Form Non SSL Password


    too_many_sessions (optional, any, None)
      Too many sessions consumed


    buf_ovf_hdr_value_len_fail (optional, any, None)
      Buffer Overflow - Header Value Length Failure


    uri_blist_succ (optional, any, None)
      URI Black List Success


    sess_check_fail (optional, any, None)
      Session Check Failure


    buf_ovf_hdr_name_len_fail (optional, any, None)
      Buffer Overflow - Header Name Length Failure


    resp_denied (optional, any, None)
      Responses Denied


    sessions_freed (optional, any, None)
      Sessions freed


    out_of_sessions (optional, any, None)
      Out of sessions


    xml_limit_elem (optional, any, None)
      XML Limit Element


    buf_ovf_parameter_name_len_fail (optional, any, None)
      Buffer Overflow - HTML Parameter Name Length Failure


    xml_limit_attr_value_len (optional, any, None)
      XML Limit Value Length


    xml_limit_elem_depth (optional, any, None)
      XML Limit Element Depth


    ccn_mask_jcb (optional, any, None)
      Credit Card Number Mask Jcb


    cookie_decrypt_fail (optional, any, None)
      Cookie Decrypt Failure


    buf_ovf_cookie_value_len_fail (optional, any, None)
      Buffer Overflow - Cookie Value Length Failure


    buf_ovf_post_size_fail (optional, any, None)
      Buffer Overflow - Post size Failure


    total_req (optional, any, None)
      Total Requests


    xml_limit_elem_name_len (optional, any, None)
      XML Limit Element Name Length


    url_check_learn (optional, any, None)
      URL Check Learn


    http_method_check_succ (optional, any, None)
      Http Method Check Success


    xss_chk_url_succ (optional, any, None)
      XSS Check URL Success


    xml_limit_namespace_uri_len (optional, any, None)
      XML Limit Namespace URI Length


    post_form_check_reject (optional, any, None)
      Post Form Check Rejected


    cookie_encrypt_fail (optional, any, None)
      Cookie Encrypt Failure


    soap_check_failure (optional, any, None)
      Soap Check Failure


    challenge_captcha_sent (optional, any, None)
      Captcha challenge sent


    form_csrf_tag_fail (optional, any, None)
      Form CSRF tag Failure


    xml_xss_chk_succ (optional, any, None)
      XML XSS Check Success


    buf_ovf_max_data_parse_fail (optional, any, None)
      Buffer Overflow - Max Data Parse Failure



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


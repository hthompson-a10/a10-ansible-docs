.. _a10_waf_template_module:


a10_waf_template -- Configures A10 waf.template
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Manage WAF template configuration






Parameters
----------

  form_deny_non_ssl (False, any, None)
    Deny request with forms if the protocol is not SSL


  remove_spaces (False, any, None)
    Remove spaces from internal url


  max_parameter_name_len (False, any, None)
    Max HTML parameter name length in an HTTP request (default 256) (Maximum HTML parameter name length in an HTTP request (default 256))


  max_namespace (False, any, None)
    Maximum number of namespace declarations (default 16)


  brute_force_resp_headers_file (False, any, None)
    Name of WAF policy list file


  max_line_len (False, any, None)
    Max Line length allowed in request (default 1024) (Maximum length of Request line allowed (default 1024))


  xml_xss_check (False, any, None)
    Check XML data against XSS policy


  http_redirect (False, any, None)
    Send HTTP redirect response (302 Found) to specifed URL (URL to redirect to when denying request)


  redirect_wlist (False, any, None)
    Check Redirect URL against list of previously learned redirects


  max_cookie_name_len (False, any, None)
    Max Cookie Name length allowed in request (default 64) ( Maximum length of cookie name allowed (default 64))


  brute_force_resp_headers (False, any, None)
    Trigger brute-force check on HTTP response header names


  sqlia_check (False, any, None)
    'reject'= Reject requests with SQLIA patterns; 'sanitize'= Remove bad SQL from request;


  waf_wlist_file (False, any, None)
    Name of WAF policy list file


  max_entities (False, any, None)
    Maximum number of MIME entities allowed in request (default 10)


  uuid (False, any, None)
    uuid of the object


  deploy_mode (False, any, None)
    'active'= Deploy WAF in active (blocking) mode; 'passive'= Deploy WAF in passive (log-only) mode; 'learning'= Deploy WAF in learning mode;


  max_elem_child (False, any, None)
    Maximum number of children of an XML element (default 1024)


  challenge_action_cookie (False, any, None)
    Use Set-Cookie to determine if client allows cookies


  referer_safe_url (False, any, None)
     Safe URL to redirect to if referer is missing


  max_hdrs (False, any, None)
    Maximum number of headers allowed in request (default 20)


  max_parameter_total_len (False, any, None)
    Max HTML parameter total length in an HTTP request (default 4096) (Maximum HTML parameter total length in an HTTP request (default 4096))


  decode_escaped_chars (False, any, None)
    Decode escaped characters such as \r \n \' \xXX \u00YY in internal url


  waf_blist_file (False, any, None)
    Name of WAF policy list file


  referer_domain_list_only (False, any, None)
    List of referer domains allowed


  uri_wlist_check (False, any, None)
    specify name of WAF policy list file to whitelist


  allowed_http_methods (False, any, None)
    List of allowed HTTP methods. Default is 'GET POST'. (List of HTTP methods allowed (default 'GET POST'))


  max_depth (False, any, None)
    Maximum recursion depth in a value in a JSON requesnt body (default 16) (Maximum recursion depth in a JSON value (default 16))


  user_tag (False, any, None)
    Customized tag


  reset_conn (False, any, None)
    Reset the client connection


  deny_non_masked_passwords (False, any, None)
    Denies forms that have a password field with a textual type, resulting in this field not being masked


  hide_resp_codes_file (False, any, None)
    Name of WAF policy list file


  session_check (False, any, None)
    Enable session checking via session cookie


  http_resp_200 (False, any, None)
    Send HTTP response with status code 200 OK


  log_succ_reqs (False, any, None)
    Log successful waf requests


  wsdl_file (False, any, None)
    Specify name of WSDL file for verifying XML body contents


  brute_force_check (False, any, None)
    Enable brute-force attack mitigation


  form_deny_non_post (False, any, None)
    Deny request with forms if the method is not POST


  ccn_mask (False, any, None)
    Mask credit card numbers in response


  remove_selfref (False, any, None)
    Remove self-references such as /./ and /path/../ from internal url


  url_check (False, any, None)
    Check URL against list of previously learned URLs


  max_cdata_len (False, any, None)
    Maximum length of an CDATA section of an element (default 65535)


  referer_check (False, any, None)
    Check referer to protect against CSRF attacks


  challenge_action_javascript (False, any, None)
    Add JavaScript to response to test if client allows JavaScript


  max_cookie_value_len (False, any, None)
    Max Cookie Value length allowed in request (default 4096) (Maximum length of cookie value allowed (default 4096))


  ansible_port (True, any, None)
    Port for AXAPI authentication


  max_url_len (False, any, None)
    Max URL length allowed in request (default 1024) (Maximum length of URL allowed (default 1024))


  name (True, any, None)
    WAF Template Name


  max_object_member_count (False, any, None)
    Maximum number of members in an object in a JSON request body (default 256) (Maximum number of members in a JSON object (default 256))


  max_array_value_count (False, any, None)
    Maximum number of values in an array in a JSON request body (default 256) (Maximum number of values in a JSON array (default 256))


  brute_force_resp_codes (False, any, None)
    Trigger brute-force check on HTTP response code


  bot_check (False, any, None)
    Check User-Agent for known bots


  brute_force_challenge_limit (False, any, None)
    Maximum brute-force events before sending challenge (default 2) (Maximum brute- force events before locking out client (default 2))


  http_check (False, any, None)
    Check request for HTTP protocol compliance


  max_hdr_name_len (False, any, None)
    Max header name length allowed in request (default 63) (Maximum length of header name allowed (default 63))


  remove_comments (False, any, None)
    Remove comments from internal url


  ssn_mask (False, any, None)
    Mask US Social Security numbers in response


  pcre_mask (False, any, None)
    Mask matched PCRE pattern in response


  max_elem_depth (False, any, None)
    Maximum recursion level for element definition (default 256)


  soap_format_check (False, any, None)
    Check XML document for SOAP format compliance


  brute_force_global (False, any, None)
    Brute-force triggers apply globally instead of per-client (Apply brute-force triggers globally)


  brute_force_resp_string_file (False, any, None)
    Name of WAF policy list file


  ansible_password (True, any, None)
    Password for AXAPI authentication


  max_namespace_uri_len (False, any, None)
    Maximum length of a namespace URI (default 256)


  xss_check (False, any, None)
    'reject'= Reject requests with bad cookies; 'sanitize'= Remove bad cookies from request;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  form_consistency_check (False, any, None)
    Form input consistency check


  hide_resp_codes (False, any, None)
    Hides response codes that are not allowed (default 4xx, 5xx)


  brute_force_lockout_period (False, any, None)
    Number of seconds client should be locked out (default 600)


  decode_hex_chars (False, any, None)
    Decode hex chars such as \%xx and \%u00yy in internal url


  max_parameter_value_len (False, any, None)
    Max HTML parameter value length in an HTTP request (default 4096) (Maximum HTML parameter value in an HTTP request (default 4096))


  max_elem (False, any, None)
    Maximum number of XML elements (default 1024)


  lifetime (False, any, None)
    Session lifetime in minutes (default 10)


  sqlia_check_policy_file (False, any, None)
    Name of WAF policy list file


  brute_force_resp_string (False, any, None)
    Trigger brute-force check on HTTP response line


  http_resp_403 (False, any, None)
    Send HTTP response with status code 403 Forbidden (default)


  referer_domain_list (False, any, None)
    List of referer domains allowed


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


    name (optional, any, None)
      WAF Template Name


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



  csrf_check (False, any, None)
    Tag the form to protect against Cross-site Request Forgery


  max_data_parse (False, any, None)
    Max data parsed for Web Application Firewall (default 65536) (Maximum data parsed for Web Application Firewall (default 65536))


  xml_format_check (False, any, None)
    Check HTTP body for XML format compliance


  cookie_encryption_secret (False, any, None)
    Cookie encryption secret


  state (True, any, None)
    State of the object to be created.


  filter_resp_hdrs (False, any, None)
    Removes web server's identifying headers


  max_cookies (False, any, None)
    Maximum number of cookies allowed in request (default 20)


  max_elem_name_len (False, any, None)
    Maximum length for an element name (default 128)


  max_post_size (False, any, None)
    Max content length allowed in POST request (default 20480) (Maximum size allowed content in an HTTP POST request (default 20480))


  form_set_no_cache (False, any, None)
    Disable caching of form-containing responses


  max_attr (False, any, None)
    Maximum number of attributes of an XML element (default 256)


  deny_password_autocomplete (False, any, None)
    Check to protect against server-generated form which contain password fields that allow autocomplete


  max_attr_name_len (False, any, None)
    Maximum length of an attribute name (default 128)


  xss_check_policy_file (False, any, None)
    Name of WAF policy list file


  resp_url_403 (False, any, None)
    Response content to send client when denying request


  uri_blist_check (False, any, None)
    specify name of WAF policy list file to blacklist


  max_string (False, any, None)
    Maximum length of a string in a JSON request body (default 64) (Maximum length of a JSON string (default 64))


  max_entity_exp (False, any, None)
    Maximum number of entity expansions (default 1024)


  cookie_name (False, any, None)
    Cookie name (simple string or PCRE pattern)


  max_hdrs_len (False, any, None)
    Max headers length allowed in request (default 4096) (Maximum length of headers allowed (default 4096))


  xml_schema_resp_val_file (False, any, None)
    Specify name of XML-Schema file for verifying XML body contents


  xml_schema_file (False, any, None)
    Specify name of XML-Schema file for verifying XML body contents


  brute_force_resp_codes_file (False, any, None)
    Name of WAF policy list file


  disable (False, any, None)
    Disable buffer overflow protection


  deny_non_ssl_passwords (False, any, None)
    Denies any form that has a password field if the form is not sent over an SSL connection


  bot_check_policy_file (False, any, None)
    Name of WAF policy list file


  brute_force_test_period (False, any, None)
    Number of seconds for brute-force event counting (default 60)


  max_parameters (False, any, None)
    Maximum number of HTML parameters allowed in request (default 64)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  max_hdr_value_len (False, any, None)
    Max header value length allowed in request (default 4096) (Maximum length of header value allowed (default 4096))


  max_cookie_len (False, any, None)
    Max Cookie length allowed in request (default 4096) (Maximum length of cookie allowed (default 4096))


  logging (False, any, None)
    Logging template (Logging Config name)


  max_cookies_len (False, any, None)
    Max Total Cookies length allowed in request (default 4096) (Maximum total length of cookies allowed (default 4096))


  max_query_len (False, any, None)
    Max Query length allowed in request (default 1024) (Maximum length of Request query allowed (default 1024))


  decode_entities (False, any, None)
    Decode entities in internal url


  keep_start (False, any, None)
    Number of unmasked characters at the beginning (default= 0)


  mask (False, any, None)
    Character to mask the matched pattern (default= X)


  wsdl_resp_val_file (False, any, None)
    Specify name of WSDL file for verifying XML body contents


  max_entity_exp_depth (False, any, None)
    Maximum nested depth of entity expansion (default 32)


  resp_url_200 (False, any, None)
    Response content to send client when denying request


  json_format_check (False, any, None)
    Check HTTP body for JSON format compliance


  xml_sqlia_check (False, any, None)
    Check XML data against SQLIA policy


  brute_force_lockout_limit (False, any, None)
    Maximum brute-force events before locking out client (default 5)


  max_attr_value_len (False, any, None)
    Maximum length of an attribute text value (default 128)


  secret_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)


  keep_end (False, any, None)
    Number of unmasked characters at the end (default= 0)









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


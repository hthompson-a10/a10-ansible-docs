.. _a10_aam_authorization_policy_module:


a10_aam_authorization_policy -- Configures A10 aam.authorization.policy
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Authorization-policy configuration






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  forward_policy_authorize_only (False, any, None)
    This policy only provides server info for forward policy feature


  jwt_claim_map_list (False, any, None)
    Field jwt_claim_map_list


    claim (optional, any, None)
      Specify JWT claim name to map to.


    str_val (optional, any, None)
      Specify JWT claim value.


    uuid (optional, any, None)
      uuid of the object


    boolean_type (optional, any, None)
      Claim type is boolean


    ntype (optional, any, None)
      Specify claim type


    string_type (optional, any, None)
      Claim type is string


    attr_num (optional, any, None)
      Spcify attribute ID for claim mapping


    number_type (optional, any, None)
      Claim type is number


    bool_val (optional, any, None)
      'true'= True; 'false'= False;


    num_val (optional, any, None)
      Specify JWT claim value.



  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  service_group (False, any, None)
    Specify an authentication service group for authorization (Specify authentication service group name)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  extended_filter (False, any, None)
    Extended search filter. EX= Check whether user belongs to a nested group. (memberOf=1.2.840.113556.1.4.1941==$GROUP-DN)


  name (True, any, None)
    Specify authorization policy name


  attribute_rule (False, any, None)
    Define attribute rule for authorization policy


  jwt_authorization (False, any, None)
    Specify JWT authorization template (Specify JWT authorization template name)


  attribute_list (False, any, None)
    Field attribute_list


    attr_str_val (optional, any, None)
      Set attribute value


    custom_attr_type (optional, any, None)
      Specify attribute type


    attr_int (optional, any, None)
      'equal'= Operation type is equal; 'not-equal'= Operation type is not equal; 'less-than'= Operation type is less-than; 'more-than'= Operation type is more- than; 'less-than-equal-to'= Operation type is less-than-equal-to; 'more-than- equal-to'= Operation type is more-thatn-equal-to;


    string_type (optional, any, None)
      Attribute type is string


    integer_type (optional, any, None)
      Attribute type is integer


    attr_num (optional, any, None)
      Set attribute ID for authorization policy


    A10_AX_AUTH_URI (optional, any, None)
      Custom-defined attribute


    attr_str (optional, any, None)
      'match'= Operation type is match; 'sub-string'= Operation type is sub-string;


    custom_attr_str (optional, any, None)
      'match'= Operation type is match; 'sub-string'= Operation type is sub-string;


    any (optional, any, None)
      Matched when attribute is present (with any value).


    ip_type (optional, any, None)
      IP address is transformed into network byte order


    attr_ip (optional, any, None)
      'equal'= Operation type is equal; 'not-equal'= Operation type is not-equal;


    attribute_name (optional, any, None)
      Specify attribute name


    uuid (optional, any, None)
      uuid of the object


    attr_int_val (optional, any, None)
      Set attribute value


    attr_ipv4 (optional, any, None)
      IPv4 address


    a10_dynamic_defined (optional, any, None)
      The value of this attribute will depend on AX configuration instead of user configuration


    attr_type (optional, any, None)
      Specify attribute type



  server (False, any, None)
    Specify a LDAP or RADIUS server for authorization (Specify a LDAP or RADIUS server name)


  state (True, any, None)
    State of the object to be created.


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


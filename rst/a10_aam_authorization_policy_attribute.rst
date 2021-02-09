.. _a10_aam_authorization_policy_attribute_module:


a10_aam_authorization_policy_attribute -- Configures A10 aam.authorization.policy.attribute
===========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Authorization-policy attribute configuration






Parameters
----------

  attr_str_val (False, any, None)
    Set attribute value


  ansible_username (True, any, None)
    Username for AXAPI authentication


  custom_attr_type (False, any, None)
    Specify attribute type


  A10_AX_AUTH_URI (False, any, None)
    Custom-defined attribute


  string_type (False, any, None)
    Attribute type is string


  policy_name (optional, any, None)
    Key to identify parent object


  integer_type (False, any, None)
    Attribute type is integer


  attr_num (True, any, None)
    Set attribute ID for authorization policy


  attr_int (False, any, None)
    'equal'= Operation type is equal; 'not-equal'= Operation type is not equal; 'less-than'= Operation type is less-than; 'more-than'= Operation type is more- than; 'less-than-equal-to'= Operation type is less-than-equal-to; 'more-than- equal-to'= Operation type is more-thatn-equal-to;


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  attr_str (False, any, None)
    'match'= Operation type is match; 'sub-string'= Operation type is sub-string;


  custom_attr_str (False, any, None)
    'match'= Operation type is match; 'sub-string'= Operation type is sub-string;


  a10_partition (False, any, None)
    Destination/target partition for object/command


  any (False, any, None)
    Matched when attribute is present (with any value).


  attr_ip (False, any, None)
    'equal'= Operation type is equal; 'not-equal'= Operation type is not-equal;


  ansible_port (True, any, None)
    Port for AXAPI authentication


  attribute_name (False, any, None)
    Specify attribute name


  uuid (False, any, None)
    uuid of the object


  a10_dynamic_defined (False, any, None)
    The value of this attribute will depend on AX configuration instead of user configuration


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  attr_int_val (False, any, None)
    Set attribute value


  attr_ipv4 (False, any, None)
    IPv4 address


  ip_type (False, any, None)
    IP address is transformed into network byte order


  ansible_password (True, any, None)
    Password for AXAPI authentication


  attr_type (False, any, None)
    Specify attribute type









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


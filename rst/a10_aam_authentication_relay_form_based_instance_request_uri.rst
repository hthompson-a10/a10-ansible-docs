.. _a10_aam_authentication_relay_form_based_instance_request_uri_module:


a10_aam_authentication_relay_form_based_instance_request_uri -- Configures A10 aam.authentication.relay.form.based.instance.request-uri
=======================================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

URI of authentication web page






Parameters
----------

  match_type (True, any, None)
    'equals'= URI exactly matches the string; 'contains'= URI string contains another sub string; 'starts-with'= URI string starts with sub string; 'ends- with'= URI string ends with sub string;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_variable (False, any, None)
    Specify username variable name


  domain_variable (False, any, None)
    Specify domain variable name


  action_uri (False, any, None)
    Specify the action-URI


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  user_tag (False, any, None)
    Customized tag


  other_variables (False, any, None)
    Specify other variables (n1=v1&n2=v2) in form relay


  uri (True, any, None)
    Specify request URI


  instance_name (optional, any, None)
    Key to identify parent object


  state (True, any, None)
    State of the object to be created.


  password_variable (False, any, None)
    Specify password variable name


  cookie (False, any, None)
    Field cookie


    cookie_value (optional, any, None)
      Field cookie_value



  ansible_password (True, any, None)
    Password for AXAPI authentication


  max_packet_collect_size (False, any, None)
    Specify the max packet collection size in bytes, default is 1MB









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


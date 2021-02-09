.. _a10_slb_template_smtp_module:


a10_slb_template_smtp -- Configures A10 slb.template.smtp
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SMTP






Parameters
----------

  client_starttls_type (False, any, None)
    'optional'= STARTTLS is optional requirement; 'enforced'= Must issue STARTTLS command before mail transaction;


  ansible_username (True, any, None)
    Username for AXAPI authentication


  LF_to_CRLF (False, any, None)
    Change the LF to CRLF for smtp end of line


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  server_domain (False, any, None)
    Config the domain of the email servers (Server's domain, default is 'mail- server-domain')


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  command_disable (False, any, None)
    Field command_disable


    disable_type (optional, any, None)
      'expn'= Disable SMTP EXPN commands; 'turn'= Disable SMTP TURN commands; 'vrfy'= Disable SMTP VRFY commands;



  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    SMTP Template Name


  error_code_to_client (False, any, None)
    Would transfer error code(554) to client, when getting it from connection establishing with real-server


  state (True, any, None)
    State of the object to be created.


  server_starttls_type (False, any, None)
    'optional'= STARTTLS is optional requirement; 'enforced'= Must issue STARTTLS command before mail transaction;


  service_ready_msg (False, any, None)
    Set SMTP service ready message (SMTP service ready message, default is 'ESMTP mail service ready')


  template (False, any, None)
    Field template


    logging (optional, any, None)
      Logging template (Logging Config name)



  user_tag (False, any, None)
    Customized tag


  client_domain_switching (False, any, None)
    Field client_domain_switching


    service_group (optional, any, None)
      Select service group (Service group name)


    switching_type (optional, any, None)
      'contains'= Specify domain name string if domain contains another string; 'ends-with'= Specify domain name string if domain ends with another string; 'starts-with'= Specify domain string if domain starts with another string;


    match_string (optional, any, None)
      Domain name string










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


.. _a10_slb_template_imap_pop3_module:


a10_slb_template_imap_pop3 -- Configures A10 slb.template.imap-pop3
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

IMAP






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    IMAP-POP3 Template Name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  starttls (False, any, None)
    'disabled'= Disable STARTTLS; 'optional'= STARTTLS is optional requirement; 'enforced'= Must issue STARTTLS command before imap transaction;


  state (True, any, None)
    State of the object to be created.


  logindisabled (False, any, None)
    Disable Login before STARTTLS.Works only for imap


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  uuid (False, any, None)
    uuid of the object









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


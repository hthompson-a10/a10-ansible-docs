.. _a10_slb_template_smpp_module:


a10_slb_template_smpp -- Configures A10 slb.template.smpp
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

SMPP template






Parameters
----------

  server_selection_per_request (False, any, None)
    Force server selection on every SMPP request when enable conn-reuse


  ansible_username (True, any, None)
    Username for AXAPI authentication


  server_enquire_link (False, any, None)
    Send server ENQUIRE_LINK packet for every persist connection when enable conn- reuse


  user (False, any, None)
    Configure the user to bind (The name used to bind)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  password (False, any, None)
    Configure the password used to bind


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    SMPP Template Name


  ansible_password (True, any, None)
    Password for AXAPI authentication


  server_enquire_link_val (False, any, None)
    Set interval of keep-alive packet for each persistent connection (second, default is 30)


  state (True, any, None)
    State of the object to be created.


  user_tag (False, any, None)
    Customized tag


  client_enquire_link (False, any, None)
    Respond client ENQUIRE_LINK packet directly instead of forwarding to server









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


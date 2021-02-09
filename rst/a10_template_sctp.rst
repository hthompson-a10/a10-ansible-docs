.. _a10_template_sctp_module:


a10_template_sctp -- Configures A10 template.sctp
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Define a SCTP template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    SCTP Template Name


  permit_payload_protocol (False, any, None)
    Field permit_payload_protocol


    permit_config_id (optional, any, None)
      Field permit_config_id


    permit_config_name (optional, any, None)
      Field permit_config_name



  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  checksum_check (False, any, None)
    'enable'= Enable Checksum check;


  user_tag (False, any, None)
    Customized tag


  state (True, any, None)
    State of the object to be created.


  log (False, any, None)
    Field log


    payload_proto_filtering (optional, any, None)
      Log Payload Protocol IDs Filtered



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  sctp_half_open_idle_timeout (False, any, None)
    Set SCTP half-open timeout (SCTP half-open timeout in seconds (default 4))


  sctp_idle_timeout (False, any, None)
    SCTP idle timeout in minutes (default 5)


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


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


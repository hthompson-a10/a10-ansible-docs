.. _a10_cgnv6_sctp_permit_payload_protocol_protocol_name_module:


a10_cgnv6_sctp_permit_payload_protocol_protocol_name -- Configures A10 cgnv6.sctp.permit.payload.protocol.protocol-name
=======================================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure SCTP permitted payload protocols






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  protocol (True, any, None)
    'iua'= IUA; 'm2ua'= M2UA; 'm3ua'= M3UA; 'sua'= SUA; 'm2pa'= M2PA; 'h.323'= H.323;


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


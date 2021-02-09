.. _a10_delete_glm_license_module:


a10_delete_glm_license -- Configures A10 delete.glm-license
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Remove glm license






Parameters
----------

  qosmos (False, any, None)
    only remove QOSMOS license


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  webroot_ti (False, any, None)
    only remove Webroot Threat Intel license


  cylance (False, any, None)
    only remove Cylance license


  threatstop (False, any, None)
    only remove ThreatSTOP license


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ipsec_vpn (False, any, None)
    only remove IPSEC VPN license


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


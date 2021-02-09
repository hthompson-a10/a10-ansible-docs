.. _a10_slb_ssl_sni_automap_attributes_module:


a10_slb_ssl_sni_automap_attributes -- Configures A10 slb.ssl.sni-automap-attributes
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Server Name Automap global settings






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  sni_lower_limit (False, any, None)
    Lower limit for free SNI contexts count. Default is 500


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  sni_upper_limit (False, any, None)
    Upper limit for free SNI contexts count. Default is 2000


  a10_partition (False, any, None)
    Destination/target partition for object/command


  sni_delete_factor (False, any, None)
    Contexts are deleted in groups of this value. Default is 50









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


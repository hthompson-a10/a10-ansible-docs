.. _a10_slb_template_diameter_origin_host_module:


a10_slb_template_diameter_origin_host -- Configures A10 slb.template.diameter.origin-host
=========================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

origin host name avp






Parameters
----------

  diameter_name (optional, any, None)
    Key to identify parent object


  ansible_port (True, any, None)
    Port for AXAPI authentication


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


  origin_host_name (False, any, None)
    origin-host name avp


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


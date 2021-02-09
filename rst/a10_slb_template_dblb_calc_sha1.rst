.. _a10_slb_template_dblb_calc_sha1_module:


a10_slb_template_dblb_calc_sha1 -- Configures A10 slb.template.dblb.calc-sha1
=============================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Calculate sha1 value of a cleartext password






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  sha1_value (False, any, None)
    Cleartext password


  state (True, any, None)
    State of the object to be created.


  dblb_name (optional, any, None)
    Key to identify parent object


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


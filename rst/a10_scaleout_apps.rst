.. _a10_scaleout_apps_module:


a10_scaleout_apps -- Configures A10 scaleout.apps
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable Scaleout for apps






Parameters
----------

  skip_mac_overwrite (False, any, None)
    Field skip_mac_overwrite


    enable (optional, any, None)
      Skips overwriting dest MAC of flooded packets on Active node


    uuid (optional, any, None)
      uuid of the object



  ansible_port (True, any, None)
    Port for AXAPI authentication


  enable (False, any, None)
    Enable Scaleout for apps


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


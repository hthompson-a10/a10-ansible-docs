.. _a10_automatic_update_info_module:


a10_automatic_update_info -- Configures A10 automatic.update.info
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

automatic-update information opers






Parameters
----------

  oper (False, any, None)
    Field oper


    feature_list (optional, any, None)
      Field feature_list



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    dummy (optional, any, None)
      Entry for a10countergen



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


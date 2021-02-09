.. _a10_upgrade_cf_module:


a10_upgrade_cf -- Configures A10 upgrade.cf
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Compact flash






Parameters
----------

  reboot_after_upgrade (False, any, None)
    reboot system after upgrade is done


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  local (False, any, None)
    Use image from local VCS image repository (Specify an image name, format= aximage_XX_XX_XX_XX.tar.gz)


  image (False, any, None)
    'pri'= Primary image;


  file_url (False, any, None)
    File URL


  ansible_password (True, any, None)
    Password for AXAPI authentication


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  state (True, any, None)
    State of the object to be created.


  staggered_upgrade_mode (False, any, None)
    in staggered upgrade mode


  use_mgmt_port (False, any, None)
    Use management port as source port


  Device (False, any, None)
    Field Device


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


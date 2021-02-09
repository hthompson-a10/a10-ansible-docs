.. _a10_upgrade_hd_module:


a10_upgrade_hd -- Configures A10 upgrade.hd
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Hard Disk






Parameters
----------

  rollback (False, any, None)
    Field rollback


  ansible_username (True, any, None)
    Username for AXAPI authentication


  image (False, any, None)
    'pri'= Primary image; 'sec'= Secondary image;


  source_ip_address (False, any, None)
    Source ip address


  staggered_upgrade_mode (False, any, None)
    in staggered upgrade mode


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  reboot_after_upgrade (False, any, None)
    reboot system after upgrade is done


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  file_url (False, any, None)
    File URL


  state (True, any, None)
    State of the object to be created.


  Device (False, any, None)
    Field Device


  local (False, any, None)
    Use image from local VCS image repository (Specify an image name, format= aximage_XX_XX_XX_XX.tar.gz)









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


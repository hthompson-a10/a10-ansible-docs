.. _a10_upgrade_gui_module:


a10_upgrade_gui -- Configures A10 upgrade.gui
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Upgrade or Rollback GUI






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  rollback (False, any, None)
    Rollback to a specific local GUI image


  ansible_username (True, any, None)
    Username for AXAPI authentication


  local (False, any, None)
    Local GUI image name


  image (False, any, None)
    'pri'= Primary image; 'sec'= Secondary image;


  file_url (False, any, None)
    File URL


  upload (False, any, None)
    Upload GUI image from remote


  source_ip_address (False, any, None)
    Source IP address


  state (True, any, None)
    State of the object to be created.


  use_mgmt_port (False, any, None)
    Use management port as source port


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  delete (False, any, None)
    Delete one local GUI image









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


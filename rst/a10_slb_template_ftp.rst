.. _a10_slb_template_ftp_module:


a10_slb_template_ftp -- Configures A10 slb.template.ftp
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

FTP template






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  name (True, any, None)
    FTP template name


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  active_mode_port_val (False, any, None)
    Non-Standard FTP Active mode port


  active_mode_port (False, any, None)
    Non-Standard FTP Active mode port


  ansible_host (True, any, None)
    Host for AXAPI authentication


  to (False, any, None)
    End range of FTP Active mode port


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  any (False, any, None)
    Allow any FTP Active mode port


  user_tag (False, any, None)
    Customized tag


  uuid (False, any, None)
    uuid of the object









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


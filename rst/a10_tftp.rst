.. _a10_tftp_module:


a10_tftp -- Configures A10 tftp
===============================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

TFTP client configuration






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


  state (True, any, None)
    State of the object to be created.


  blksize (False, any, None)
    TFTP client block size value (Block size (Blksize/Max file size. Example= 1K/64M, 8K/512M, 32K/2048M),default is 32768)


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


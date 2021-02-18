.. _a10_pki_copy_key_module:


a10_pki_copy_key -- Configures A10 pki.copy-key
===============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Copy SSL key to another file






Parameters
----------

+-----------------------+---------------------+----------------------------------------------------+
| Parameters            | Choices/Defaults    | Comment                                            |
|                       |                     |                                                    |
|                       |                     |                                                    |
+=======================+=====================+====================================================+
| state                 | ['noop', 'present'] | State of the object to be created.                 |
|                       |                     |                                                    |
| /required             |                     |                                                    |
+-----------------------+---------------------+----------------------------------------------------+
| ansible_host          |                     | Host for AXAPI authentication                      |
|                       |                     |                                                    |
| /required             |                     |                                                    |
+-----------------------+---------------------+----------------------------------------------------+
| ansible_username      |                     | Username for AXAPI authentication                  |
|                       |                     |                                                    |
| /required             |                     |                                                    |
+-----------------------+---------------------+----------------------------------------------------+
| ansible_password      |                     | Password for AXAPI authentication                  |
|                       |                     |                                                    |
| /required             |                     |                                                    |
+-----------------------+---------------------+----------------------------------------------------+
| ansible_port          |                     | Port for AXAPI authentication                      |
|                       |                     |                                                    |
| /required             |                     |                                                    |
+-----------------------+---------------------+----------------------------------------------------+
| a10_device_context_id | ['1-8']             | Device ID for aVCS configuration                   |
|                       |                     |                                                    |
|                       |                     |                                                    |
+-----------------------+---------------------+----------------------------------------------------+
| a10_partition         |                     | Destination/target partition for object/command    |
|                       |                     |                                                    |
|                       |                     |                                                    |
+-----------------------+---------------------+----------------------------------------------------+
| src_key               |                     | Source key file                                    |
|                       |                     |                                                    |
|                       |                     |                                                    |
+-----------------------+---------------------+----------------------------------------------------+
| rotation              |                     | Specify rotation number of SCEP generated key file |
|                       |                     |                                                    |
|                       |                     |                                                    |
+-----------------------+---------------------+----------------------------------------------------+
| dest_key              |                     | Destination key file                               |
|                       |                     |                                                    |
|                       |                     |                                                    |
+-----------------------+---------------------+----------------------------------------------------+
| overwrite             |                     | Overwrite the destination file if already present  |
|                       |                     |                                                    |
|                       |                     |                                                    |
+-----------------------+---------------------+----------------------------------------------------+







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


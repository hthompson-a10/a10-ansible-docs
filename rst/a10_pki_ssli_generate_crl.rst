.. _a10_pki_ssli_generate_crl_module:


a10_pki_ssli_generate_crl -- Configures A10 pki.ssli.generate.crl
=================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Generate a CRL for for a vport






Parameters
----------

+-----------------------+---------------------+-------------------------------------------------+
| Parameters            | Choices/Defaults    | Comment                                         |
|                       |                     |                                                 |
|                       |                     |                                                 |
+=======================+=====================+=================================================+
| state                 | ['noop', 'present'] | State of the object to be created.              |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| ansible_host          |                     | Host for AXAPI authentication                   |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| ansible_username      |                     | Username for AXAPI authentication               |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| ansible_password      |                     | Password for AXAPI authentication               |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| ansible_port          |                     | Port for AXAPI authentication                   |
|                       |                     |                                                 |
| /required             |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| a10_device_context_id | ['1-8']             | Device ID for aVCS configuration                |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| a10_partition         |                     | Destination/target partition for object/command |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| vip_name              |                     | VIP name                                        |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+
| port                  |                     | port number                                     |
|                       |                     |                                                 |
|                       |                     |                                                 |
+-----------------------+---------------------+-------------------------------------------------+







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


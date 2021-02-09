.. _a10_mirror_port_module:


a10_mirror_port -- Configures A10 mirror-port
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable a port to act as Mirror Port






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  mirror_dir (False, any, None)
    'input'= Mirror incoming packets to this port; 'output'= Mirror outgoing packets to this port; 'both'= Mirror both incoming and outgoing packets to this port;


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  mirror_index (True, any, None)
    Mirror index


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ethernet (False, any, None)
    Ethernet port as mirror port (Port Value)


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


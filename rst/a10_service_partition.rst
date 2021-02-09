.. _a10_service_partition_module:


a10_service_partition -- Configures A10 service-partition
=========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create/unload a service partition






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  application_type (False, any, None)
    'adc'= Application type ADC;


  follow_vrid (False, any, None)
    Join a vrrp group (Specify ha VRRP-A vrid)


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  partition_name (True, any, None)
    Object service partition name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  id (False, any, None)
    Specify unique service partition id


  user_tag (False, any, None)
    Customized tag









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


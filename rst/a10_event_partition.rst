.. _a10_event_partition_module:


a10_event_partition -- Configures A10 event.partition
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

module partition






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  logging (False, any, None)
    'on'= enable this action; 'off'= disable this action;


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  vnp_events (True, any, None)
    'part-create'= Create new partition; 'part-del'= Delete a partition;


  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  email (False, any, None)
    'on'= enable this action; 'off'= disable this action;









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


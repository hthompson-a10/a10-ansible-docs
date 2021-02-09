.. _a10_network_bpdu_fwd_group_module:


a10_network_bpdu_fwd_group -- Configures A10 network.bpdu-fwd-group
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

STP BPDU forward Group Settings






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  ansible_username (True, any, None)
    Username for AXAPI authentication


  user_tag (False, any, None)
    Customized tag


  ansible_password (True, any, None)
    Password for AXAPI authentication


  bpdu_fwd_group_number (True, any, None)
    Field bpdu_fwd_group_number


  state (True, any, None)
    State of the object to be created.


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ethernet_list (False, any, None)
    Field ethernet_list


    ethernet_start (optional, any, None)
      Ethernet Port (Interface number)


    ethernet_end (optional, any, None)
      Ethernet Port



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


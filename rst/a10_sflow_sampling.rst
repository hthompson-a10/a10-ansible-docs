.. _a10_sflow_sampling_module:


a10_sflow_sampling -- Configures A10 sflow.sampling
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Configure sFlow sampling on specified interfaces






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


  eth_list (False, any, None)
    Field eth_list


    eth_start (optional, any, None)
      Ethernet interface to sample


    eth_end (optional, any, None)
      Ethernet interface to sample



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  ve_list (False, any, None)
    Field ve_list


    ve_start (optional, any, None)
      VE interface to sample


    ve_end (optional, any, None)
      VE interface to sample



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


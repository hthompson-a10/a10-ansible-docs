.. _a10_multi_ctrl_cpu_module:


a10_multi_ctrl_cpu -- Configures A10 multi-ctrl-cpu
===================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Enable Multiple Control CPUs






Parameters
----------

  ansible_port (True, any, None)
    Port for AXAPI authentication


  num_ctrl_cpus (False, any, None)
    Set number of control CPUs. Default is 1, and max limit is platform dependent.


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ansible_password (True, any, None)
    Password for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


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


.. _a10_system_environment_module:


a10_system_environment -- Configures A10 system.environment
===========================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Field environment






Parameters
----------

  oper (False, any, None)
    Field oper


    fan9a_value (optional, any, None)
      Field fan9a_value


    fan3a_value (optional, any, None)
      Field fan3a_value


    fan10a_report (optional, any, None)
      Field fan10a_report


    fan3a_report (optional, any, None)
      Field fan3a_report


    physical_temperature (optional, any, None)
      Field physical_temperature


    fan6b_value (optional, any, None)
      Field fan6b_value


    fan4b_report (optional, any, None)
      Field fan4b_report


    fan8a_value (optional, any, None)
      Field fan8a_value


    fan2a_report (optional, any, None)
      Field fan2a_report


    fan2b_value (optional, any, None)
      Field fan2b_value


    fan1b_report (optional, any, None)
      Field fan1b_report


    fan1a_value (optional, any, None)
      Field fan1a_value


    fan4b_value (optional, any, None)
      Field fan4b_value


    fan8a_report (optional, any, None)
      Field fan8a_report


    fan4a_value (optional, any, None)
      Field fan4a_value


    fan1b_value (optional, any, None)
      Field fan1b_value


    fan2a_value (optional, any, None)
      Field fan2a_value


    fan5b_value (optional, any, None)
      Field fan5b_value


    fan9b_report (optional, any, None)
      Field fan9b_report


    fan8b_report (optional, any, None)
      Field fan8b_report


    power_unit4 (optional, any, None)
      Field power_unit4


    power_unit3 (optional, any, None)
      Field power_unit3


    fan3b_report (optional, any, None)
      Field fan3b_report


    power_unit1 (optional, any, None)
      Field power_unit1


    fan6a_report (optional, any, None)
      Field fan6a_report


    fan8b_value (optional, any, None)
      Field fan8b_value


    fan7b_report (optional, any, None)
      Field fan7b_report


    fan5a_value (optional, any, None)
      Field fan5a_value


    power_unit2 (optional, any, None)
      Field power_unit2


    voltage_label_17 (optional, any, None)
      Field voltage_label_17


    voltage_label_16 (optional, any, None)
      Field voltage_label_16


    voltage_label_15 (optional, any, None)
      Field voltage_label_15


    voltage_label_14 (optional, any, None)
      Field voltage_label_14


    voltage_label_13 (optional, any, None)
      Field voltage_label_13


    voltage_label_12 (optional, any, None)
      Field voltage_label_12


    fan5a_report (optional, any, None)
      Field fan5a_report


    fan9b_value (optional, any, None)
      Field fan9b_value


    voltage_label_8 (optional, any, None)
      Field voltage_label_8


    voltage_label_11 (optional, any, None)
      Field voltage_label_11


    fan7a_report (optional, any, None)
      Field fan7a_report


    fan1a_report (optional, any, None)
      Field fan1a_report


    voltage_label_10 (optional, any, None)
      Field voltage_label_10


    fan6b_report (optional, any, None)
      Field fan6b_report


    fan3b_value (optional, any, None)
      Field fan3b_value


    voltage_label_9 (optional, any, None)
      Field voltage_label_9


    fan5b_report (optional, any, None)
      Field fan5b_report


    fan6a_value (optional, any, None)
      Field fan6a_value


    fan2b_report (optional, any, None)
      Field fan2b_report


    voltage_label_2 (optional, any, None)
      Field voltage_label_2


    voltage_label_1 (optional, any, None)
      Field voltage_label_1


    voltage_label_7 (optional, any, None)
      Field voltage_label_7


    voltage_label_6 (optional, any, None)
      Field voltage_label_6


    voltage_label_5 (optional, any, None)
      Field voltage_label_5


    voltage_label_4 (optional, any, None)
      Field voltage_label_4


    voltage_label_3 (optional, any, None)
      Field voltage_label_3


    fan9a_report (optional, any, None)
      Field fan9a_report


    physical_temperature2 (optional, any, None)
      Field physical_temperature2


    fan7a_value (optional, any, None)
      Field fan7a_value


    fan10a_value (optional, any, None)
      Field fan10a_value


    fan10b_value (optional, any, None)
      Field fan10b_value


    fan7b_value (optional, any, None)
      Field fan7b_value


    fan4a_report (optional, any, None)
      Field fan4a_report


    fan10b_report (optional, any, None)
      Field fan10b_report



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


.. _a10_health_monitor_method_database_module:


a10_health_monitor_method_database -- Configures A10 health.monitor.method.database
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

DATABASE type






Parameters
----------

  db_send (False, any, None)
    Specify the SQL query


  db_receive (False, any, None)
    Specify the response string


  ansible_username (True, any, None)
    Username for AXAPI authentication


  db_row (False, any, None)
    Specify the row number for receiving


  db_encrypted (False, any, None)
    Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)


  db_column_integer (False, any, None)
    Specify the column number for receiving


  db_name (False, any, None)
    Specify the database name


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  monitor_name (optional, any, None)
    Key to identify parent object


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  db_password_str (False, any, None)
    Configure password


  uuid (False, any, None)
    uuid of the object


  db_column (False, any, None)
    Specify the column number for receiving


  database (False, any, None)
    DATABASE type


  a10_partition (False, any, None)
    Destination/target partition for object/command


  database_name (False, any, None)
    'mssql'= Specify MSSQL database; 'mysql'= Specify MySQL database; 'oracle'= Specify Oracle database; 'postgresql'= Specify PostgreSQL database;


  db_row_integer (False, any, None)
    Specify the row number for receiving


  state (True, any, None)
    State of the object to be created.


  db_username (False, any, None)
    Specify the username


  db_password (False, any, None)
    Specify the user password


  db_receive_integer (False, any, None)
    Specify the response integer


  ansible_password (True, any, None)
    Password for AXAPI authentication









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


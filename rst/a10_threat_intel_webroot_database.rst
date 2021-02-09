.. _a10_threat_intel_webroot_database_module:


a10_threat_intel_webroot_database -- Configures A10 threat.intel.webroot-database
=================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

webroot database information






Parameters
----------

  oper (False, any, None)
    Field oper


    status (optional, any, None)
      Field status


    last_update_time (optional, any, None)
      Field last_update_time


    botnets (optional, any, None)
      Field botnets


    version (optional, any, None)
      Field version


    proxy (optional, any, None)
      Field proxy


    last_successful_connection (optional, any, None)
      Field last_successful_connection


    spam_sources (optional, any, None)
      Field spam_sources


    reputation (optional, any, None)
      Field reputation


    size (optional, any, None)
      Field size


    connection_status (optional, any, None)
      Field connection_status


    name (optional, any, None)
      Field name


    next_update_time (optional, any, None)
      Field next_update_time


    phishing (optional, any, None)
      Field phishing


    total_entries (optional, any, None)
      Field total_entries


    web_attacks (optional, any, None)
      Field web_attacks


    failure_reason (optional, any, None)
      Field failure_reason


    mobile_threats (optional, any, None)
      Field mobile_threats


    dos_attacks (optional, any, None)
      Field dos_attacks


    tor_proxy (optional, any, None)
      Field tor_proxy


    scanners (optional, any, None)
      Field scanners


    windows_exploits (optional, any, None)
      Field windows_exploits



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


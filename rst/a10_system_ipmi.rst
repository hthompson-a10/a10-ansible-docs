.. _a10_system_ipmi_module:


a10_system_ipmi -- Configures A10 system.ipmi
=============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Perform IPMI related operations






Parameters
----------

  reset (False, any, None)
    Reset IPMI Controller


  ansible_port (True, any, None)
    Port for AXAPI authentication


  ansible_username (True, any, None)
    Username for AXAPI authentication


  ip (False, any, None)
    Field ip


    ipv4_address (optional, any, None)
      IP address


    ipv4_netmask (optional, any, None)
      IP subnet mask


    default_gateway (optional, any, None)
      Default gateway address



  ipsrc (False, any, None)
    Field ipsrc


    dhcp (optional, any, None)
      IP addr obtained by BMC running DHCP


    static (optional, any, None)
      Manually configured static IP address



  ansible_password (True, any, None)
    Password for AXAPI authentication


  ansible_host (True, any, None)
    Host for AXAPI authentication


  state (True, any, None)
    State of the object to be created.


  user (False, any, None)
    Field user


    administrator (optional, any, None)
      Full control


    setname (optional, any, None)
      Change User Name (Current IPMI User Name)


    newname (optional, any, None)
      New IPMI User Name


    add (optional, any, None)
      Add a new IPMI user (IPMI User Name)


    callback (optional, any, None)
      Lowest privilege level


    newpass (optional, any, None)
      New Password


    disable (optional, any, None)
      Disable an existing IPMI user (IPMI User Name)


    setpass (optional, any, None)
      Change Password (IPMI User Name)


    user (optional, any, None)
      Only 'benign' commands are allowed


    operator (optional, any, None)
      Most BMC commands are allowed


    password (optional, any, None)
      Password


    privilege (optional, any, None)
      Change an existing IPMI user privilege (IPMI User Name)



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  tool (False, any, None)
    Field tool


    cmd (optional, any, None)
      Command to execute in double quotes










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


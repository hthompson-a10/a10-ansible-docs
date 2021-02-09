.. _a10_terminal_module:


a10_terminal -- Configures A10 terminal
=======================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Set Terminal Startup Parameters






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  idle_timeout (False, any, None)
    Set interval for closing connection when there is no input detected (Timeout in minutes, 0 means never timeout, default is 15)


  gslb_cfg (False, any, None)
    Field gslb_cfg


    gslb_prompt (optional, any, None)
      The gslb status prompt function set


    disable (optional, any, None)
      Group status show disable


    symbol (optional, any, None)
      Show 'gslb' symbol on CLI prompt


    group_role (optional, any, None)
      Show GSLB group role on CLI prompt



  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  auto_size (False, any, None)
    Enable terminal length and width automatically (not work if width or length set to 0)


  editing (False, any, None)
    Enable command line editing


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  length (False, any, None)
    Set number of lines on a screen(0 for no pausing) (Number of lines on screen, 0 for no pausing, default is 24)


  history_cfg (False, any, None)
    Field history_cfg


    enable (optional, any, None)
      Enable terminal history


    size (optional, any, None)
      Set history buffer size (Size of history buffer, default is 256)



  width (False, any, None)
    Set width of the display terminal (Number of characters on a screen line, 0 means infinite, default is 80)


  state (True, any, None)
    State of the object to be created.


  prompt_cfg (False, any, None)
    Field prompt_cfg


    prompt (optional, any, None)
      Configure the normal prompt format


    hostname (optional, any, None)
      Display hostname in prompt


    vcs_cfg (optional, any, None)
      Field vcs_cfg



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


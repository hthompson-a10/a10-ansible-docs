.. _a10_aam_authentication_portal_logon_fail_module:


a10_aam_authentication_portal_logon_fail -- Configures A10 aam.authentication.portal.logon-fail
===============================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Logon fail page configuration






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


  portal_name (optional, any, None)
    Key to identify parent object


  fail_msg_cfg (False, any, None)
    Field fail_msg_cfg


    fail_color_name (optional, any, None)
      'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow;


    fail_font_custom (optional, any, None)
      Specify custom font


    fail_color (optional, any, None)
      Specify font color (Default= black)


    fail_msg (optional, any, None)
      Configure logon failure message in default logon fail page


    fail_face (optional, any, None)
      'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;


    fail_size (optional, any, None)
      Specify font size (Default= 3)


    fail_color_value (optional, any, None)
      Specify 6-digit HEX color value


    fail_font (optional, any, None)
      Sepcify font (Default= Arial)


    fail_text (optional, any, None)
      Specify logon failure message (Default= Login Failed!!)



  state (True, any, None)
    State of the object to be created.


  title_cfg (False, any, None)
    Field title_cfg


    title_size (optional, any, None)
      Specify font size (Default= 5)


    title_color (optional, any, None)
      Specify font color (Default= black)


    title (optional, any, None)
      Configure title in default logon fail page


    title_face (optional, any, None)
      'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;


    title_color_value (optional, any, None)
      Specify 6-digit HEX color value


    title_text (optional, any, None)
      Specify title (Default= Try Too Many Times)


    title_color_name (optional, any, None)
      'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow;


    title_font (optional, any, None)
      Sepcify font (Default= Arial)


    title_font_custom (optional, any, None)
      Specify custom font



  background (False, any, None)
    Field background


    bgcolor_name (optional, any, None)
      'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow;


    bgfile (optional, any, None)
      Specify background image filename


    bgstyle (optional, any, None)
      'tile'= Tile; 'stretch'= Stretch; 'fit'= Fit;


    bgcolor_value (optional, any, None)
      Specify 6-digit HEX color value



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


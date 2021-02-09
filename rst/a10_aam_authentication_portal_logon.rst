.. _a10_aam_authentication_portal_logon_module:


a10_aam_authentication_portal_logon -- Configures A10 aam.authentication.portal.logon
=====================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Logon page configuration






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  portal_name (optional, any, None)
    Key to identify parent object


  passcode_cfg (False, any, None)
    Field passcode_cfg


    passcode_face (optional, any, None)
      'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;


    passcode_color_value (optional, any, None)
      Specify 6-digit HEX color value


    passcode_size (optional, any, None)
      Specify font size (Default= 3)


    passcode_font_custom (optional, any, None)
      Specify custom font


    passcode_text (optional, any, None)
      Specify passcode text (Default= Passcode)


    passcode_color (optional, any, None)
      Specify font color (Default= black)


    passcode_font (optional, any, None)
      Sepcify font (Default= Arial)


    passcode (optional, any, None)
      Configure passcode text in default logon page


    passcode_color_name (optional, any, None)
      'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow;



  fail_msg_cfg (False, any, None)
    Field fail_msg_cfg


    fail_color_name (optional, any, None)
      'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow;


    fail_font_custom (optional, any, None)
      Specify custom font


    fail_color (optional, any, None)
      Specify font color (Default= red)


    fail_msg (optional, any, None)
      Configure login failure message in default logon page


    fail_face (optional, any, None)
      'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;


    fail_size (optional, any, None)
      Specify font size (Default= 5)


    fail_color_value (optional, any, None)
      Specify 6-digit HEX color value


    authz_fail_msg (optional, any, None)
      Configure authorization failure message in default logon page, its text attributes follow fail-msg's (Specify authorization failure message (Default= Authorization failed. Please contact your system administrator.))


    fail_font (optional, any, None)
      Sepcify font (Default= Arial)


    fail_text (optional, any, None)
      Specify login failure message (Default= Invalid username or password. Please try again.)



  action_url (False, any, None)
    Specify form action URL in default logon page (Default= /logon.fo)


  password_cfg (False, any, None)
    Field password_cfg


    pass_size (optional, any, None)
      Specify font size (Default= 3)


    pass_face (optional, any, None)
      'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;


    pass_font_custom (optional, any, None)
      Specify custom font


    pass_text (optional, any, None)
      Specify password text (Default= Password)


    pass_color (optional, any, None)
      Specify font color (Default= black)


    pass_color_name (optional, any, None)
      'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow;


    pass_color_value (optional, any, None)
      Specify 6-digit HEX color value


    pass_font (optional, any, None)
      Sepcify font (Default= Arial)


    password (optional, any, None)
      Configure password text in default logon page



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


  submit_text (False, any, None)
    Specify submit button text in default logon page (Default= Log In)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  uuid (False, any, None)
    uuid of the object


  username_var (False, any, None)
    Specify username variable name in default logon page (Default= user)


  username_cfg (False, any, None)
    Field username_cfg


    username (optional, any, None)
      Configure username text in default logon page


    user_font (optional, any, None)
      Sepcify font (Default= Arial)


    user_color (optional, any, None)
      Specify font color (Default= black)


    user_text (optional, any, None)
      Specify username text (Default= User Name)


    user_color_name (optional, any, None)
      'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow;


    user_face (optional, any, None)
      'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;


    user_size (optional, any, None)
      Specify font size (Default= 3)


    user_color_value (optional, any, None)
      Specify 6-digit HEX color value


    user_font_custom (optional, any, None)
      Specify custom font



  passcode_var (False, any, None)
    Specify passcode variable name in default logon page (Default= passcode)


  enable_passcode (False, any, None)
    Enable passcode field in default logon page


  state (True, any, None)
    State of the object to be created.


  password_var (False, any, None)
    Specify password variable name in default logon page (Default= pwd)


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


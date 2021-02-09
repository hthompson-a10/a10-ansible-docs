.. _a10_aam_authentication_portal_change_password_module:


a10_aam_authentication_portal_change_password -- Configures A10 aam.authentication.portal.change-password
=========================================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Change password page configuration






Parameters
----------

  ansible_username (True, any, None)
    Username for AXAPI authentication


  portal_name (optional, any, None)
    Key to identify parent object


  action_url (False, any, None)
    Specify form action URL in default change password page (Default= /change.fo)


  old_pwd_cfg (False, any, None)
    Field old_pwd_cfg


    old_face (optional, any, None)
      'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;


    old_text (optional, any, None)
      Specify old password text (Default= Old Password)


    old_font (optional, any, None)
      Sepcify font (Default= Arial)


    old_color_value (optional, any, None)
      Specify 6-digit HEX color value


    old_size (optional, any, None)
      Specify font size (Default= 3)


    old_color (optional, any, None)
      Specify font color (Default= black)


    old_color_name (optional, any, None)
      'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow;


    old_font_custom (optional, any, None)
      Specify custom font


    old_password (optional, any, None)
      Configure old password text in default change password page



  title_cfg (False, any, None)
    Field title_cfg


    title_size (optional, any, None)
      Specify font size (Default= 5)


    title_color (optional, any, None)
      Specify font color (Default= black)


    title (optional, any, None)
      Configure title in default change password page


    title_face (optional, any, None)
      'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;


    title_color_value (optional, any, None)
      Specify 6-digit HEX color value


    title_text (optional, any, None)
      Specify title (Default= Please Change Your Password)


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



  reset_text (False, any, None)
    Specify reset button text in default change password page (Default= Reset)


  a10_device_context_id (False, any, None)
    Device ID for aVCS configuration


  a10_partition (False, any, None)
    Destination/target partition for object/command


  ansible_host (True, any, None)
    Host for AXAPI authentication


  submit_text (False, any, None)
    Specify submit button text in default change password page (Default= Submit)


  ansible_port (True, any, None)
    Port for AXAPI authentication


  cfm_pwd_cfg (False, any, None)
    Field cfm_pwd_cfg


    confirm_password (optional, any, None)
      Configure confirm password text in default change password page


    cfm_font (optional, any, None)
      Sepcify font (Default= Arial)


    cfm_font_custom (optional, any, None)
      Specify custom font


    cfm_color_value (optional, any, None)
      Specify 6-digit HEX color value


    cfm_size (optional, any, None)
      Specify font size (Default= 3)


    cfm_color_name (optional, any, None)
      'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow;


    cfm_color (optional, any, None)
      Specify font color (Default= black)


    cfm_face (optional, any, None)
      'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;


    cfm_text (optional, any, None)
      Specify confirm password text (Default= Confirm New Password)



  uuid (False, any, None)
    uuid of the object


  username_var (False, any, None)
    Specify username variable name in default change password page (Default= cp_usr)


  old_password_var (False, any, None)
    Specify old password variable name in default change password page (Default= cp_old_pwd)


  new_pwd_cfg (False, any, None)
    Field new_pwd_cfg


    new_color_name (optional, any, None)
      'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray; 'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive; 'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal; 'white'= white; 'yellow'= yellow;


    new_text (optional, any, None)
      Specify new password text (Default= New Password)


    new_face (optional, any, None)
      'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia; 'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;


    new_font (optional, any, None)
      Sepcify font (Default= Arial)


    new_password (optional, any, None)
      Configure new password text in default change password page


    new_font_custom (optional, any, None)
      Specify custom font


    new_size (optional, any, None)
      Specify font size (Default= 3)


    new_color (optional, any, None)
      Specify font color (Default= black)


    new_color_value (optional, any, None)
      Specify 6-digit HEX color value



  username_cfg (False, any, None)
    Field username_cfg


    username (optional, any, None)
      Configure username text in default change password page


    user_font (optional, any, None)
      Sepcify font (Default= Arial)


    user_color (optional, any, None)
      Specify font color (Default= black)


    user_text (optional, any, None)
      Specify username text (Default= Username)


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



  state (True, any, None)
    State of the object to be created.


  new_password_var (False, any, None)
    Specify new password variable name in default change password page (Default= cp_new_pwd)


  confirm_password_var (False, any, None)
    Specify confirm password variable name in default change password page (Default= cp_cfm_pwd)


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


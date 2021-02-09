.. _a10_system_tcp_module:


a10_system_tcp -- Configures A10 system.tcp
===========================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

tcp counters






Parameters
----------

  sampling_enable (False, any, None)
    Field sampling_enable


    counters1 (optional, any, None)
      'all'= all; 'activeopens'= Active open conns; 'passiveopens'= Passive open conns; 'attemptfails'= Connect attemp failures; 'estabresets'= Resets rcvd on EST conn; 'insegs'= Total in TCP packets; 'outsegs'= Total out TCP packets; 'retranssegs'= Retransmited packets; 'inerrs'= Input errors; 'outrsts'= Reset Sent; 'sock_alloc'= Sockets allocated; 'orphan_count'= Orphan sockets; 'mem_alloc'= Memory alloc; 'recv_mem'= Total rx buffer; 'send_mem'= Total tx buffer; 'currestab'= Currently EST conns; 'currsyssnt'= TCP in SYN-SNT state; 'currsynrcv'= TCP in SYN-RCV state; 'currfinw1'= TCP in FIN-W1 state; 'currfinw2'= TCP FIN-W2 state; 'currtimew'= TCP TimeW state; 'currclose'= TCP in Close state; 'currclsw'= TCP in CloseW state; 'currlack'= TCP in LastACK state; 'currlstn'= TCP in Listen state; 'currclsg'= TCP in Closing state; 'pawsactiverejected'= TCP paw active rej; 'syn_rcv_rstack'= Rcv RST|ACK on SYN; 'syn_rcv_rst'= Rcv RST on SYN; 'syn_rcv_ack'= Rcv ACK on SYN; 'ax_rexmit_syn'= TCP rexmit SYN; 'tcpabortontimeout'= TCP abort on timeout; 'noroute'= TCPIP out noroute; 'exceedmss'= MSS exceeded pkt dropped; 'tfo_conns'= TFO Total Connections; 'tfo_actives'= TFO Current Actives; 'tfo_denied'= TFO Denied;



  oper (False, any, None)
    Field oper


    tcp_cpu_list (optional, any, None)
      Field tcp_cpu_list


    cpu_count (optional, any, None)
      Field cpu_count



  ansible_port (True, any, None)
    Port for AXAPI authentication


  stats (False, any, None)
    Field stats


    sampling_enable (optional, any, None)
      Field sampling_enable


    uuid (optional, any, None)
      uuid of the object



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


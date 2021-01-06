.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.bvitnik.xenserver.xenserver_guest_powerstate_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

bvitnik.xenserver.xenserver_guest_powerstate -- Manages power states of virtual machines running on Citrix Hypervisor/XenServer host or pool
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `bvitnik.xenserver collection <https://galaxy.ansible.com/bvitnik/xenserver>`_ (version 1.0.0).

    To install it use: :code:`ansible-galaxy collection install bvitnik.xenserver`.

    To use it in a playbook, specify: :code:`bvitnik.xenserver.xenserver_guest_powerstate`.

.. version_added

.. versionadded:: 1.0.0 of bvitnik.xenserver

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module can be used to power on, power off, restart or suspend virtual machine and gracefully reboot or shutdown guest OS of virtual machine.



.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 2.6
- XenAPI


.. Options

Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"localhost"</div>
                                    </td>
                                                                <td>
                                            <div>The hostname or IP address of the XenServer host or XenServer pool master.</div>
                                            <div>If the value is not specified in the task, the value of environment variable <code>XENSERVER_HOST</code> will be used instead.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: host, pool</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the VM to manage.</div>
                                            <div>VMs running on XenServer do not necessarily have unique names. The module will fail if multiple VMs with same name are found.</div>
                                            <div>In case of multiple VMs with same name, use <code>uuid</code> to uniquely specify VM to manage.</div>
                                            <div>This parameter is case sensitive.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name_label</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-password"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The password to use for connecting to XenServer.</div>
                                            <div>If the value is not specified in the task, the value of environment variable <code>XENSERVER_PASSWORD</code> will be used instead.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: pass, pwd</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>powered-on</li>
                                                                                                                                                                                                <li>powered-off</li>
                                                                                                                                                                                                <li>restarted</li>
                                                                                                                                                                                                <li>shutdown-guest</li>
                                                                                                                                                                                                <li>reboot-guest</li>
                                                                                                                                                                                                <li>suspended</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specify the state VM should be in.</div>
                                            <div>If <code>state</code> is set to value other than <code>present</code>, then VM is transitioned into required state and facts are returned.</div>
                                            <div>If <code>state</code> is set to <code>present</code>, then VM is just checked for existence and facts are returned.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-state_change_timeout"></div>
                    <b>state_change_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-state_change_timeout" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">0</div>
                                    </td>
                                                                <td>
                                            <div>By default, module will wait indefinitely for VM to change state or acquire an IP address if <code>wait_for_ip_address: yes</code>.</div>
                                            <div>If this parameter is set to positive value, the module will instead wait specified number of seconds for the state change.</div>
                                            <div>In case of timeout, module will generate an error message.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-username"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"root"</div>
                                    </td>
                                                                <td>
                                            <div>The username to use for connecting to XenServer.</div>
                                            <div>If the value is not specified in the task, the value of environment variable <code>XENSERVER_USER</code> will be used instead.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: admin, user</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-uuid"></div>
                    <b>uuid</b>
                    <a class="ansibleOptionLink" href="#parameter-uuid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>UUID of the VM to manage if known. This is XenServer&#x27;s unique identifier.</div>
                                            <div>It is required if name is not unique.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Allows connection when SSL certificates are not valid. Set to <code>false</code> when certificates are not trusted.</div>
                                            <div>If the value is not specified in the task, the value of environment variable <code>XENSERVER_VALIDATE_CERTS</code> will be used instead.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-wait_for_ip_address"></div>
                    <b>wait_for_ip_address</b>
                    <a class="ansibleOptionLink" href="#parameter-wait_for_ip_address" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Wait until XenServer detects an IP address for the VM.</div>
                                            <div>This requires XenServer Tools to be preinstalled on the VM to work properly.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>

.. Notes

Notes
-----

.. note::
   - Minimal supported version of XenServer is 5.6.
   - Module was tested with XenServer 6.5, 7.1, 7.2, 7.6, Citrix Hypervisor 8.0, XCP-ng 7.6 and 8.0.
   - To acquire XenAPI Python library, just run ``pip install XenAPI`` on your Ansible Control Node. The library can also be found inside Citrix Hypervisor/XenServer SDK (downloadable from Citrix website). Copy the XenAPI.py file from the SDK to your Python site-packages on your Ansible Control Node to use it. Latest version of the library can also be acquired from GitHub: https://raw.githubusercontent.com/xapi-project/xen-api/master/scripts/examples/python/XenAPI/XenAPI.py
   - If no scheme is specified in ``hostname``, module defaults to ``http://`` because ``https://`` is problematic in most setups. Make sure you are accessing XenServer host in trusted environment or use ``https://`` scheme explicitly.
   - To use ``https://`` scheme for ``hostname`` you have to either import host certificate to your OS certificate store or use ``validate_certs: no`` which requires XenAPI library from XenServer 7.2 SDK or newer and Python 2.7.9 or newer.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Power on VM
      bvitnik.xenserver.xenserver_guest_powerstate:
        hostname: "{{ xenserver_hostname }}"
        username: "{{ xenserver_username }}"
        password: "{{ xenserver_password }}"
        name: testvm_11
        state: powered-on
      delegate_to: localhost
      register: facts




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-instance"></div>
                    <b>instance</b>
                    <a class="ansibleOptionLink" href="#return-instance" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Metadata about the VM</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;cdrom&#x27;: {&#x27;type&#x27;: &#x27;none&#x27;}, &#x27;customization_agent&#x27;: &#x27;native&#x27;, &#x27;disks&#x27;: [{&#x27;name&#x27;: &#x27;windows-template-testing-0&#x27;, &#x27;name_desc&#x27;: &#x27;&#x27;, &#x27;os_device&#x27;: &#x27;xvda&#x27;, &#x27;size&#x27;: 42949672960, &#x27;sr&#x27;: &#x27;Local storage&#x27;, &#x27;sr_uuid&#x27;: &#x27;0af1245e-bdb0-ba33-1446-57a962ec4075&#x27;, &#x27;vbd_userdevice&#x27;: &#x27;0&#x27;}, {&#x27;name&#x27;: &#x27;windows-template-testing-1&#x27;, &#x27;name_desc&#x27;: &#x27;&#x27;, &#x27;os_device&#x27;: &#x27;xvdb&#x27;, &#x27;size&#x27;: 42949672960, &#x27;sr&#x27;: &#x27;Local storage&#x27;, &#x27;sr_uuid&#x27;: &#x27;0af1245e-bdb0-ba33-1446-57a962ec4075&#x27;, &#x27;vbd_userdevice&#x27;: &#x27;1&#x27;}], &#x27;domid&#x27;: &#x27;56&#x27;, &#x27;folder&#x27;: &#x27;&#x27;, &#x27;hardware&#x27;: {&#x27;memory_mb&#x27;: 8192, &#x27;num_cpu_cores_per_socket&#x27;: 2, &#x27;num_cpus&#x27;: 4}, &#x27;home_server&#x27;: &#x27;&#x27;, &#x27;is_template&#x27;: False, &#x27;name&#x27;: &#x27;windows-template-testing&#x27;, &#x27;name_desc&#x27;: &#x27;&#x27;, &#x27;networks&#x27;: [{&#x27;gateway&#x27;: &#x27;192.168.0.254&#x27;, &#x27;gateway6&#x27;: &#x27;fc00::fffe&#x27;, &#x27;ip&#x27;: &#x27;192.168.0.200&#x27;, &#x27;ip6&#x27;: [&#x27;fe80:0000:0000:0000:e9cb:625a:32c5:c291&#x27;, &#x27;fc00:0000:0000:0000:0000:0000:0000:0001&#x27;], &#x27;mac&#x27;: &#x27;ba:91:3a:48:20:76&#x27;, &#x27;mtu&#x27;: &#x27;1500&#x27;, &#x27;name&#x27;: &#x27;Pool-wide network associated with eth1&#x27;, &#x27;netmask&#x27;: &#x27;255.255.255.128&#x27;, &#x27;prefix&#x27;: &#x27;25&#x27;, &#x27;prefix6&#x27;: &#x27;64&#x27;, &#x27;vif_device&#x27;: &#x27;0&#x27;}], &#x27;other_config&#x27;: {&#x27;base_template_name&#x27;: &#x27;Windows Server 2016 (64-bit)&#x27;, &#x27;import_task&#x27;: &#x27;OpaqueRef:e43eb71c-45d6-5351-09ff-96e4fb7d0fa5&#x27;, &#x27;install-methods&#x27;: &#x27;cdrom&#x27;, &#x27;instant&#x27;: &#x27;true&#x27;, &#x27;mac_seed&#x27;: &#x27;f83e8d8a-cfdc-b105-b054-ef5cb416b77e&#x27;}, &#x27;platform&#x27;: {&#x27;acpi&#x27;: &#x27;1&#x27;, &#x27;apic&#x27;: &#x27;true&#x27;, &#x27;cores-per-socket&#x27;: &#x27;2&#x27;, &#x27;device_id&#x27;: &#x27;0002&#x27;, &#x27;hpet&#x27;: &#x27;true&#x27;, &#x27;nx&#x27;: &#x27;true&#x27;, &#x27;pae&#x27;: &#x27;true&#x27;, &#x27;timeoffset&#x27;: &#x27;-25200&#x27;, &#x27;vga&#x27;: &#x27;std&#x27;, &#x27;videoram&#x27;: &#x27;8&#x27;, &#x27;viridian&#x27;: &#x27;true&#x27;, &#x27;viridian_reference_tsc&#x27;: &#x27;true&#x27;, &#x27;viridian_time_ref_count&#x27;: &#x27;true&#x27;}, &#x27;state&#x27;: &#x27;poweredon&#x27;, &#x27;uuid&#x27;: &#x27;e3c0b2d5-5f05-424e-479c-d3df8b3e7cda&#x27;, &#x27;xenstore_data&#x27;: {&#x27;vm-data&#x27;: &#x27;&#x27;}}</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>

..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Bojan Vitnik (@bvitnik) <bvitnik@mainstream.rs>



.. Parsing errors


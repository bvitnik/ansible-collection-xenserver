.. Document meta

:orphan:

.. Anchors

.. _ansible_collections.bvitnik.xenserver.xenserver_guest_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

bvitnik.xenserver.xenserver_guest -- Manages virtual machines running on Citrix Hypervisor/XenServer host or pool
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `bvitnik.xenserver collection <https://galaxy.ansible.com/bvitnik/xenserver>`_ (version 1.0.0).

    To install it use: :code:`ansible-galaxy collection install bvitnik.xenserver`.

    To use it in a playbook, specify: :code:`bvitnik.xenserver.xenserver_guest`.

.. version_added

.. versionadded:: 1.0.0 of bvitnik.xenserver

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module can be used to create new virtual machines from templates or other virtual machines, modify various virtual machine components like network and disk, rename a virtual machine and remove a virtual machine with associated components.



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
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-cdrom"></div>
                    <b>cdrom</b>
                    <a class="ansibleOptionLink" href="#parameter-cdrom" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A CD-ROM configuration for the VM.</div>
                                            <div>All parameters are case sensitive.</div>
                                            <div>Valid parameters are:</div>
                                            <div>- <code>type</code> (string): The type of CD-ROM, valid options are <code>none</code> or <code>iso</code>. With <code>none</code> the CD-ROM device will be present but empty.</div>
                                            <div>- <code>iso_name</code> (string): The file name of an ISO image from one of the XenServer ISO Libraries (implies <code>type: iso</code>). Required if <code>type</code> is set to <code>iso</code>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-custom_params"></div>
                    <b>custom_params</b>
                    <a class="ansibleOptionLink" href="#parameter-custom_params" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Define a list of custom VM params to set on VM.</div>
                                            <div>Useful for advanced users familiar with managing VM params trough xe CLI.</div>
                                            <div>A custom value object takes two fields <code>key</code> and <code>value</code> (see example below).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-disks"></div>
                    <b>disks</b>
                    <a class="ansibleOptionLink" href="#parameter-disks" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of disks to add to VM.</div>
                                            <div>All parameters are case sensitive.</div>
                                            <div>Removing or detaching existing disks of VM is not supported.</div>
                                            <div>Required parameters per entry:</div>
                                            <div>- <code>size_[tb,gb,mb,kb,b]</code> (integer): Disk storage size in specified unit. VM needs to be shut down to reconfigure this parameter.</div>
                                            <div>Optional parameters per entry:</div>
                                            <div>- <code>name</code> (string): Disk name. You can also use <code>name_label</code> as an alias.</div>
                                            <div>- <code>name_desc</code> (string): Disk description.</div>
                                            <div>- <code>sr</code> (string): Storage Repository to create disk on. If not specified, will use default SR. Cannot be used for moving disk to other SR.</div>
                                            <div>- <code>sr_uuid</code> (string): UUID of a SR to create disk on. Use if SR name is not unique.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: disk</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-folder"></div>
                    <b>folder</b>
                    <a class="ansibleOptionLink" href="#parameter-folder" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Destination folder for VM.</div>
                                            <div>This parameter is case sensitive.</div>
                                            <div>Example:</div>
                                            <div>folder: /folder1/folder2</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-force"></div>
                    <b>force</b>
                    <a class="ansibleOptionLink" href="#parameter-force" title="Permalink to this option"></a>
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
                                            <div>Ignore warnings and complete the actions.</div>
                                            <div>This parameter is useful for removing VM in running state or reconfiguring VM params that require VM to be shut down.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-hardware"></div>
                    <b>hardware</b>
                    <a class="ansibleOptionLink" href="#parameter-hardware" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Manage VM&#x27;s hardware parameters. VM needs to be shut down to reconfigure these parameters.</div>
                                                        </td>
            </tr>
                                        <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hardware/memory_mb"></div>
                    <b>memory_mb</b>
                    <a class="ansibleOptionLink" href="#parameter-hardware/memory_mb" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Amount of memory in MB.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hardware/num_cpu_cores_per_socket"></div>
                    <b>num_cpu_cores_per_socket</b>
                    <a class="ansibleOptionLink" href="#parameter-hardware/num_cpu_cores_per_socket" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of Cores Per Socket. <code>num_cpus</code> has to be a multiple of <code>num_cpu_cores_per_socket</code>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-hardware/num_cpus"></div>
                    <b>num_cpus</b>
                    <a class="ansibleOptionLink" href="#parameter-hardware/num_cpus" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Number of CPUs.</div>
                                                        </td>
            </tr>
                    
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-home_server"></div>
                    <b>home_server</b>
                    <a class="ansibleOptionLink" href="#parameter-home_server" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of a XenServer host that will be a Home Server for the VM.</div>
                                            <div>This parameter is case sensitive.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-is_template"></div>
                    <b>is_template</b>
                    <a class="ansibleOptionLink" href="#parameter-is_template" title="Permalink to this option"></a>
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
                                            <div>Convert VM to template.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-linked_clone"></div>
                    <b>linked_clone</b>
                    <a class="ansibleOptionLink" href="#parameter-linked_clone" title="Permalink to this option"></a>
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
                                            <div>Whether to create a Linked Clone from the template, existing VM or snapshot. If no, will create a full copy.</div>
                                            <div>This is equivalent to <code>Use storage-level fast disk clone</code> option in XenCenter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-name"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the VM to work with.</div>
                                            <div>VMs running on XenServer do not necessarily have unique names. The module will fail if multiple VMs with same name are found.</div>
                                            <div>In case of multiple VMs with same name, use <code>uuid</code> to uniquely specify VM to manage.</div>
                                            <div>This parameter is case sensitive.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: name_label</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-name_desc"></div>
                    <b>name_desc</b>
                    <a class="ansibleOptionLink" href="#parameter-name_desc" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>VM description.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-networks"></div>
                    <b>networks</b>
                    <a class="ansibleOptionLink" href="#parameter-networks" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>                                            </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of networks (in the order of the NICs).</div>
                                            <div>All parameters are case sensitive.</div>
                                            <div>Required parameters per entry:</div>
                                            <div>- <code>name</code> (string): Name of a XenServer network to attach the network interface to. You can also use <code>name_label</code> as an alias.</div>
                                            <div>Optional parameters per entry (used for VM hardware):</div>
                                            <div>- <code>mac</code> (string): Customize MAC address of the interface.</div>
                                            <div>Optional parameters per entry (used for OS customization):</div>
                                            <div>- <code>type</code> (string): Type of IPv4 assignment, valid options are <code>none</code>, <code>dhcp</code> or <code>static</code>. Value <code>none</code> means whatever is default for OS. On some operating systems it could be DHCP configured (e.g. Windows) or unconfigured interface (e.g. Linux).</div>
                                            <div>- <code>ip</code> (string): Static IPv4 address (implies <code>type: static</code>). Can include prefix in format &lt;IPv4 address&gt;/&lt;prefix&gt; instead of using <code>netmask</code>.</div>
                                            <div>- <code>netmask</code> (string): Static IPv4 netmask required for <code>ip</code> if prefix is not specified.</div>
                                            <div>- <code>gateway</code> (string): Static IPv4 gateway.</div>
                                            <div>- <code>type6</code> (string): Type of IPv6 assignment, valid options are <code>none</code>, <code>dhcp</code> or <code>static</code>. Value <code>none</code> means whatever is default for OS. On some operating systems it could be DHCP configured (e.g. Windows) or unconfigured interface (e.g. Linux).</div>
                                            <div>- <code>ip6</code> (string): Static IPv6 address (implies <code>type6: static</code>) with prefix in format &lt;IPv6 address&gt;/&lt;prefix&gt;.</div>
                                            <div>- <code>gateway6</code> (string): Static IPv6 gateway.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: network</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-state"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                                                                                                                                <li>poweredon</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specify the state VM should be in.</div>
                                            <div>If <code>state</code> is set to <code>present</code> and VM exists, ensure the VM configuration conforms to given parameters.</div>
                                            <div>If <code>state</code> is set to <code>present</code> and VM does not exist, then VM is deployed with given parameters.</div>
                                            <div>If <code>state</code> is set to <code>absent</code> and VM exists, then VM is removed with its associated components.</div>
                                            <div>If <code>state</code> is set to <code>poweredon</code> and VM does not exist, then VM is deployed with given parameters and powered on automatically.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                            <div>By default, module will wait indefinitely for VM to accquire an IP address if <code>wait_for_ip_address: yes</code>.</div>
                                            <div>If this parameter is set to positive value, the module will instead wait specified number of seconds for the state change.</div>
                                            <div>In case of timeout, module will generate an error message.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-template"></div>
                    <b>template</b>
                    <a class="ansibleOptionLink" href="#parameter-template" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of a template, an existing VM (must be shut down) or a snapshot that should be used to create VM.</div>
                                            <div>Templates/VMs/snapshots on XenServer do not necessarily have unique names. The module will fail if multiple templates with same name are found.</div>
                                            <div>In case of multiple templates/VMs/snapshots with same name, use <code>template_uuid</code> to uniquely specify source template.</div>
                                            <div>If VM already exists, this setting will be ignored.</div>
                                            <div>This parameter is case sensitive.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: template_src</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-template_uuid"></div>
                    <b>template_uuid</b>
                    <a class="ansibleOptionLink" href="#parameter-template_uuid" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>UUID of a template, an existing VM or a snapshot that should be used to create VM.</div>
                                            <div>It is required if template name is not unique.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                            <div>Please note that a supplied UUID will be ignored on VM creation, as XenServer creates the UUID internally.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                            <div>Wait until XenServer detects an IP address for the VM. If <code>state</code> is set to <code>absent</code>, this parameter is ignored.</div>
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
   - Network configuration inside a guest OS, by using ``networks.type``, ``networks.ip``, ``networks.gateway`` etc. parameters, is supported on XenServer 7.0 or newer for Windows guests by using official XenServer Guest agent support for network configuration. The module will try to detect if such support is available and utilize it, else it will use a custom method of configuration via xenstore. Since XenServer Guest agent only support None and Static types of network configuration, where None means DHCP configured interface, ``networks.type`` and ``networks.type6`` values ``none`` and ``dhcp`` have same effect. More info here: https://www.citrix.com/community/citrix-developer/citrix-hypervisor-developer/citrix-hypervisor-developing-products/citrix-hypervisor-staticip.html
   - On platforms without official support for network configuration inside a guest OS, network parameters will be written to xenstore ``vm-data/networks/<vif_device>`` key. Parameters can be inspected by using ``xenstore ls`` and ``xenstore read`` tools on \*nix guests or trough WMI interface on Windows guests. They can also be found in VM facts ``instance.xenstore_data`` key as returned by the module. It is up to the user to implement a boot time scripts or custom agent that will read the parameters from xenstore and configure network with given parameters. Take note that for xenstore data to become available inside a guest, a VM restart is needed hence module will require VM restart if any parameter is changed. This is a limitation of XenAPI and xenstore. Considering these limitations, network configuration trough xenstore is most useful for bootstraping newly deployed VMs, much less for reconfiguring existing ones. More info here: https://support.citrix.com/article/CTX226713

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create a VM from a template
      bvitnik.xenserver.xenserver_guest:
        hostname: "{{ xenserver_hostname }}"
        username: "{{ xenserver_username }}"
        password: "{{ xenserver_password }}"
        validate_certs: no
        folder: /testvms
        name: testvm_2
        state: poweredon
        template: CentOS 7
        disks:
        - size_gb: 10
          sr: my_sr
        hardware:
          num_cpus: 6
          num_cpu_cores_per_socket: 3
          memory_mb: 512
        cdrom:
          type: iso
          iso_name: guest-tools.iso
        networks:
        - name: VM Network
          mac: aa:bb:dd:aa:00:14
        wait_for_ip_address: yes
      delegate_to: localhost
      register: deploy

    - name: Create a VM template
      bvitnik.xenserver.xenserver_guest:
        hostname: "{{ xenserver_hostname }}"
        username: "{{ xenserver_username }}"
        password: "{{ xenserver_password }}"
        validate_certs: no
        folder: /testvms
        name: testvm_6
        is_template: yes
        disk:
        - size_gb: 10
          sr: my_sr
        hardware:
          memory_mb: 512
          num_cpus: 1
      delegate_to: localhost
      register: deploy

    - name: Rename a VM (requires the VM's UUID)
      bvitnik.xenserver.xenserver_guest:
        hostname: "{{ xenserver_hostname }}"
        username: "{{ xenserver_username }}"
        password: "{{ xenserver_password }}"
        uuid: 421e4592-c069-924d-ce20-7e7533fab926
        name: new_name
        state: present
      delegate_to: localhost

    - name: Remove a VM by UUID
      bvitnik.xenserver.xenserver_guest:
        hostname: "{{ xenserver_hostname }}"
        username: "{{ xenserver_username }}"
        password: "{{ xenserver_password }}"
        uuid: 421e4592-c069-924d-ce20-7e7533fab926
        state: absent
      delegate_to: localhost

    - name: Modify custom params (boot order)
      bvitnik.xenserver.xenserver_guest:
        hostname: "{{ xenserver_hostname }}"
        username: "{{ xenserver_username }}"
        password: "{{ xenserver_password }}"
        name: testvm_8
        state: present
        custom_params:
        - key: HVM_boot_params
          value: { "order": "ndc" }
      delegate_to: localhost

    - name: Customize network parameters
      bvitnik.xenserver.xenserver_guest:
        hostname: "{{ xenserver_hostname }}"
        username: "{{ xenserver_username }}"
        password: "{{ xenserver_password }}"
        name: testvm_10
        networks:
        - name: VM Network
          ip: 192.168.1.100/24
          gateway: 192.168.1.1
        - type: dhcp
      delegate_to: localhost




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
                    <div class="ansibleOptionAnchor" id="return-changes"></div>
                    <b>changes</b>
                    <a class="ansibleOptionLink" href="#return-changes" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                       / <span style="color: purple">elements=string</span>                    </div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>Detected or made changes to VM</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;hardware&#x27;: [&#x27;num_cpus&#x27;]}, {&#x27;disks_changed&#x27;: [[], [&#x27;size&#x27;]]}, {&#x27;disks_new&#x27;: [{&#x27;name&#x27;: &#x27;new-disk&#x27;, &#x27;name_desc&#x27;: &#x27;&#x27;, &#x27;position&#x27;: 2, &#x27;size_gb&#x27;: &#x27;4&#x27;, &#x27;vbd_userdevice&#x27;: &#x27;2&#x27;}]}, {&#x27;cdrom&#x27;: [&#x27;type&#x27;, &#x27;iso_name&#x27;]}, {&#x27;networks_changed&#x27;: [[&#x27;mac&#x27;]]}, {&#x27;networks_new&#x27;: [{&#x27;name&#x27;: &#x27;Pool-wide network associated with eth2&#x27;, &#x27;position&#x27;: 1, &#x27;vif_device&#x27;: &#x27;1&#x27;}]}, &#x27;need_poweredoff&#x27;]</div>
                                    </td>
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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;cdrom&#x27;: {&#x27;type&#x27;: &#x27;none&#x27;}, &#x27;customization_agent&#x27;: &#x27;native&#x27;, &#x27;disks&#x27;: [{&#x27;name&#x27;: &#x27;testvm_11-0&#x27;, &#x27;name_desc&#x27;: &#x27;&#x27;, &#x27;os_device&#x27;: &#x27;xvda&#x27;, &#x27;size&#x27;: 42949672960, &#x27;sr&#x27;: &#x27;Local storage&#x27;, &#x27;sr_uuid&#x27;: &#x27;0af1245e-bdb0-ba33-1446-57a962ec4075&#x27;, &#x27;vbd_userdevice&#x27;: &#x27;0&#x27;}, {&#x27;name&#x27;: &#x27;testvm_11-1&#x27;, &#x27;name_desc&#x27;: &#x27;&#x27;, &#x27;os_device&#x27;: &#x27;xvdb&#x27;, &#x27;size&#x27;: 42949672960, &#x27;sr&#x27;: &#x27;Local storage&#x27;, &#x27;sr_uuid&#x27;: &#x27;0af1245e-bdb0-ba33-1446-57a962ec4075&#x27;, &#x27;vbd_userdevice&#x27;: &#x27;1&#x27;}], &#x27;domid&#x27;: &#x27;56&#x27;, &#x27;folder&#x27;: &#x27;&#x27;, &#x27;hardware&#x27;: {&#x27;memory_mb&#x27;: 8192, &#x27;num_cpu_cores_per_socket&#x27;: 2, &#x27;num_cpus&#x27;: 4}, &#x27;home_server&#x27;: &#x27;&#x27;, &#x27;is_template&#x27;: False, &#x27;name&#x27;: &#x27;testvm_11&#x27;, &#x27;name_desc&#x27;: &#x27;&#x27;, &#x27;networks&#x27;: [{&#x27;gateway&#x27;: &#x27;192.168.0.254&#x27;, &#x27;gateway6&#x27;: &#x27;fc00::fffe&#x27;, &#x27;ip&#x27;: &#x27;192.168.0.200&#x27;, &#x27;ip6&#x27;: [&#x27;fe80:0000:0000:0000:e9cb:625a:32c5:c291&#x27;, &#x27;fc00:0000:0000:0000:0000:0000:0000:0001&#x27;], &#x27;mac&#x27;: &#x27;ba:91:3a:48:20:76&#x27;, &#x27;mtu&#x27;: &#x27;1500&#x27;, &#x27;name&#x27;: &#x27;Pool-wide network associated with eth1&#x27;, &#x27;netmask&#x27;: &#x27;255.255.255.128&#x27;, &#x27;prefix&#x27;: &#x27;25&#x27;, &#x27;prefix6&#x27;: &#x27;64&#x27;, &#x27;vif_device&#x27;: &#x27;0&#x27;}], &#x27;other_config&#x27;: {&#x27;base_template_name&#x27;: &#x27;Windows Server 2016 (64-bit)&#x27;, &#x27;import_task&#x27;: &#x27;OpaqueRef:e43eb71c-45d6-5351-09ff-96e4fb7d0fa5&#x27;, &#x27;install-methods&#x27;: &#x27;cdrom&#x27;, &#x27;instant&#x27;: &#x27;true&#x27;, &#x27;mac_seed&#x27;: &#x27;f83e8d8a-cfdc-b105-b054-ef5cb416b77e&#x27;}, &#x27;platform&#x27;: {&#x27;acpi&#x27;: &#x27;1&#x27;, &#x27;apic&#x27;: &#x27;true&#x27;, &#x27;cores-per-socket&#x27;: &#x27;2&#x27;, &#x27;device_id&#x27;: &#x27;0002&#x27;, &#x27;hpet&#x27;: &#x27;true&#x27;, &#x27;nx&#x27;: &#x27;true&#x27;, &#x27;pae&#x27;: &#x27;true&#x27;, &#x27;timeoffset&#x27;: &#x27;-25200&#x27;, &#x27;vga&#x27;: &#x27;std&#x27;, &#x27;videoram&#x27;: &#x27;8&#x27;, &#x27;viridian&#x27;: &#x27;true&#x27;, &#x27;viridian_reference_tsc&#x27;: &#x27;true&#x27;, &#x27;viridian_time_ref_count&#x27;: &#x27;true&#x27;}, &#x27;state&#x27;: &#x27;poweredon&#x27;, &#x27;uuid&#x27;: &#x27;e3c0b2d5-5f05-424e-479c-d3df8b3e7cda&#x27;, &#x27;xenstore_data&#x27;: {&#x27;vm-data&#x27;: &#x27;&#x27;}}</div>
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


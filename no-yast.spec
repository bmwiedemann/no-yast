#
# spec file for package no-yast
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# Languages of the yast2-trans-* subpackages, see yast2-trans.spec
%define yast_languages af am ar ast be bg bn bs ca cs cy da de el en_GB eo es es_AR et eu fa fi fr gl gu he hi hr hu id it ja jv ka kab km kn ko ku lo lt lv mk mr ms my nb nds ne nl nn pa pl ps pt pt_BR ro ru si sk sl sq sr sr@latin sv sw ta tg th tk tr uk vi wa xh zh_CN zh_TW zu

Name:           no-yast
Version:        1.0
Release:        0
Summary:        Metapackage to keep YaST off the system
License:        MIT
Group:          System/Management
URL:            https://github.com/bmwiedemann/no-yast
Source0:        README.md
BuildArch:      noarch

# The YaST core runtime. Every yast2-* module requires at least one of these,
# so the ~90 modules need no entry of their own.
Conflicts:      yast2
Conflicts:      yast2-core
Conflicts:      yast2-logs
Conflicts:      yast2-hardware-detection
Conflicts:      yast2-pkg-bindings
Conflicts:      yast2-perl-bindings
Conflicts:      yast2-python3-bindings
Conflicts:      yast2-ruby-bindings
Conflicts:      yast2-transfer
Conflicts:      yast2-xml
Conflicts:      yast2-ycp-ui-bindings
Conflicts:      yast2-ycp-ui-bindings-dummy

# The UI layer. libyui-qt does not carry the yui_backend provide of its
# ncurses counterpart, so both backends are named explicitly. libyui_pkg is
# the Qt and NCurses package selector widget.
Conflicts:      libyui-ncurses
Conflicts:      libyui-qt
Conflicts:      libyui_pkg
Conflicts:      yui_backend
Conflicts:      yast2-control-center
Conflicts:      yast2-control-center-qt
Conflicts:      yast2-theme

# Installation and AutoYaST
Conflicts:      autoyast2
Conflicts:      autoyast2-installation
Conflicts:      yast2-installation
Conflicts:      yast2-installation-control
Conflicts:      yast2-schema
Conflicts:      yast2-schema-collection

# The YaST patterns, the usual way YaST comes back in
Conflicts:      pattern() = devel_yast
Conflicts:      pattern() = x11_yast
Conflicts:      pattern() = yast2_basis
Conflicts:      pattern() = yast2_desktop
Conflicts:      pattern() = yast2_install_wf
Conflicts:      pattern() = yast2_server

# Packages that pull in no other YaST package and would stay behind.
# yast2-qt-branding-openSUSE is built from branding-openSUSE and holds nothing
# but the artwork for the YaST Qt UI.
Conflicts:      yast2-alternatives
Conflicts:      yast2-qt-branding-openSUSE
Conflicts:      yast2-trans-stats

# Build tooling
Conflicts:      yast2-buildtools
Conflicts:      yast2-devtools
Conflicts:      yast2-testsuite

# The yast2-trans-* packages are only reachable through these provides, and
# there are too many of them to spell out.
%{lua:
for lang in string.gmatch(rpm.expand("%{yast_languages}"), "%S+") do
  print("Conflicts: locale(yast2:" .. lang .. ")\n")
end
}

%description
A metapackage that blocks the installation of YaST.

It contains no files besides its documentation. Installing it makes zypper
offer the removal of YaST, and keeps any later install, update or pattern from
pulling it back in. Removing this package lifts the block again.

See the README for the list of blocked components and for the few packages
that cannot be installed alongside it.

%prep
%autosetup -c -T
cp %{SOURCE0} .

%build

%install

%files
%doc README.md

%changelog

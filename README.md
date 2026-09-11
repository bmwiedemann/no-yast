# no-yast

A metapackage that keeps YaST off an openSUSE Tumbleweed or Slowroll system.

It ships nothing but this README. Its only content is a list of `Conflicts`
against the central YaST components, so that as long as `no-yast` is
installed, neither `zypper install`, `zypper dup` nor a pattern can pull any
part of YaST back in.

## Usage

    zypper install no-yast

If YaST is currently installed, zypper offers the removal of the conflicting
packages as a solution; pick it and the whole stack goes away in one
transaction. To get YaST back, remove the metapackage again:

    zypper remove no-yast

## What is blocked

Only the roots of the YaST dependency tree are listed, everything else follows
from them:

* the core runtime -- `yast2`, `yast2-core`, the language bindings and
  `yast2-logs`. Every `yast2-*` module requires at least one of these, so
  blocking them blocks all ~90 modules.
* the UI layer -- the `yui_backend` providers (`libyui-qt`, `libyui-ncurses`)
  and the `libyui_pkg` package selector widgets, plus the control center.
* the installer side -- `yast2-installation`, `autoyast2`, the schemas and the
  installation control file.
* the `patterns-yast-*` patterns, matched through their `pattern()` provides,
  because a pattern is the usual way YaST comes back in.
* the leftovers that depend on nothing else and would otherwise stay behind:
  `yast2-alternatives`, `yast2-theme`, `yast2-qt-branding-openSUSE` and the
  `yast2-trans-*` translations, matched through their `locale(yast2:LL)`
  provides.

`libyui` itself is deliberately not blocked. It is a generic UI abstraction
library and blocking the backends is enough to make YaST unusable.

## Known collateral damage

A few packages hard-require parts of YaST and can therefore not be installed
next to `no-yast`:

* `patterns-yast-*` -- the YaST patterns, which is the point of this package.
* `patterns-microos-base`, `patterns-aeon-base`, `patterns-kalpa-base`,
  `patterns-tik-base` -- these require `yast2-logs` for `save_y2logs`. On
  MicroOS, Aeon and Kalpa either keep YaST or drop the `yast2-logs` line from
  the spec file.
* `patterns-base-x11_raspberrypi` and the `skelcd-control-*` packages used to
  build installation media.

Ordinary Tumbleweed and Slowroll installations, including the GNOME and KDE
patterns, are unaffected -- they only `Recommend` YaST packages.

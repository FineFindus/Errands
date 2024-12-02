#!@PYTHON@

# Copyright 2023-2024 Vlad Krupinskii <mrvladus@yandex.ru>
# SPDX-License-Identifier: MIT

import os
import sys

import gi  # type: ignore


gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("Secret", "1")
gi.require_version("GtkSource", "5")
gi.require_version("Xdp", "1.0")


APP_ID = "@APP_ID@"
VERSION = "@VERSION@"
PREFIX = "@PREFIX@"
PROFILE = "@PROFILE@"
pkgdatadir = "@pkgdatadir@"
localedir = "@localedir@"


def setup_gettext():
    import gettext
    import locale
    import signal

    sys.path.insert(1, pkgdatadir)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gettext.install("errands", localedir)
    locale.bindtextdomain("errands", localedir)
    locale.textdomain("errands")


def setup_state():
    from errands.state import State

    State.PROFILE = PROFILE
    State.APP_ID = APP_ID
    State.VERSION = VERSION


def register_resources():
    from gi.repository import Gio  # type:ignore

    resource = Gio.Resource.load(os.path.join(pkgdatadir, "errands.gresource"))
    resource._register()


def main() -> None:
    setup_gettext()
    register_resources()
    setup_state()
    from errands.application import ErrandsApplication

    sys.exit(ErrandsApplication().run(sys.argv))


if __name__ == "__main__":
    main()

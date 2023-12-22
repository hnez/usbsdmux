import pathlib
import time

import pytest

from usbsdmux.usbsdmux import autoselect_driver


@pytest.fixture
def mux():
    usbsdmux_path = pathlib.Path("/dev/usb-sd-mux")

    while True:
        time.sleep(0.5)

        if not usbsdmux_path.is_dir():
            continue

        muxes = list(str(d) for d in usbsdmux_path.iterdir() if d.is_symlink())

        if len(muxes) >= 1:
            return autoselect_driver(muxes[0])


def test_switching(mux):
    print("Switch to DUT mode")
    mux.mode_DUT()

    print("Switch to host mode")
    mux.mode_host()

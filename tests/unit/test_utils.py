import sys
import os
import tempfile
import json
import pytest
from templating.utils import load_json, load_data , get_default_browser_windows

@pytest.mark.skipif(sys.platform != "win32", reason="Windows-specific test")
def test_load_json_and_load_data(tmp_path):
    # Create two JSON files
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    f1 = tmp_path / "f1.json"
    f2 = tmp_path / "f2.json"
    f1.write_text(json.dumps(d1))
    f2.write_text(json.dumps(d2))
    # Test load_json
    data1 = load_json(str(f1))
    assert data1 == d1
    # Test load_data merges correctly (d2 overrides d1)
    merged = load_data(str(f1), str(f2))
    assert merged["a"] == 1
    assert merged["b"] == 2
    assert merged["c"] == 4

@pytest.mark.skipif(sys.platform != "win32", reason="Windows-specific test")
def test_load_json_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_json("notfound.json")

@pytest.mark.skipif(sys.platform != "win32", reason="Windows-specific test")
def test_load_json_invalid_json(tmp_path):
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("{not: valid json}")
    with pytest.raises(json.JSONDecodeError):
        load_json(str(bad_file))


import types
from unittest import mock

# @pytest.mark.skipif(sys.platform != "win32", reason="Windows-specific test")
# def test_get_default_browser_windows_success():
#     # Mock winreg.OpenKey and winreg.QueryValueEx to simulate registry access
#     with mock.patch("templating.utils.winreg.OpenKey") as mock_openkey, \
#          mock.patch("templating.utils.winreg.QueryValueEx") as mock_queryvalueex:
#         mock_key = mock.MagicMock()
#         mock_openkey.return_value.__enter__.return_value = mock_key
#         mock_queryvalueex.return_value = ("ChromeHTML", None)
#         result = get_default_browser_windows()
#         assert result == "ChromeHTML"


@pytest.mark.skipif(sys.platform != "win32", reason="Windows-specific test")
def test_get_default_browser_windows_registry_error():
    # Simulate OSError when accessing registry
    with mock.patch("templating.utils.winreg.OpenKey", side_effect=OSError("Registry not found")):
        with pytest.raises(OSError):
            get_default_browser_windows()
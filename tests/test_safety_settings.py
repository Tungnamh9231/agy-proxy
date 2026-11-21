"""Regression tests for runtime Gemini safety settings."""

from unittest.mock import patch

from agy_proxy.converters.common import get_safety_settings


def test_safety_settings_default_to_block_none():
    with patch("agy_proxy.config.get_config_value", return_value="BLOCK_NONE"):
        settings = get_safety_settings()

    assert settings
    assert {item["threshold"] for item in settings} == {"BLOCK_NONE"}


def test_safety_settings_switch_to_off_dynamically():
    with patch("agy_proxy.config.get_config_value", return_value="OFF"):
        settings = get_safety_settings()

    assert settings
    assert {item["threshold"] for item in settings} == {"OFF"}


def test_invalid_saved_safety_mode_falls_back_to_block_none():
    with patch("agy_proxy.config.get_config_value", return_value="unexpected"):
        settings = get_safety_settings()

    assert settings
    assert {item["threshold"] for item in settings} == {"BLOCK_NONE"}

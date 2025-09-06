import pytest
import ssl
from urllib.error import URLError
from pyfonts.main import load_font


def make_ssl_error_urlopen(*args, **kwargs):
    raise URLError(ssl.SSLCertVerificationError("certificate verify failed"))


def test_ssl_error_raises(monkeypatch):
    monkeypatch.setattr("pyfonts.main.urlopen", make_ssl_error_urlopen)

    with pytest.raises(
        Exception, match="SSL certificate verification failed."
    ) as excinfo:
        load_font("https://example.com/font.ttf")

    msg = str(excinfo.value)
    assert "SSL certificate verification failed" in msg
    assert "danger_not_verify_ssl=True" in msg


def test_ssl_error_warning(monkeypatch):
    class DummyResponse:
        def read(self):
            return b"dummy font data"

    calls = {"count": 0}

    def fake_urlopen(*args, **kwargs):
        if calls["count"] == 0:
            calls["count"] += 1
            raise URLError(ssl.SSLCertVerificationError("certificate verify failed"))
        return DummyResponse()

    monkeypatch.setattr("pyfonts.main.urlopen", fake_urlopen)

    with pytest.warns(UserWarning, match="SSL certificate verification disabled"):
        font = load_font(
            "https://example.com/font.ttf",
            danger_not_verify_ssl=True,
            use_cache=False,
        )
        assert font is not None

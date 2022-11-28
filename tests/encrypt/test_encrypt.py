from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = encrypt_message("AABBCC", 3)
    assert "BAA_CCB" == message

    message = encrypt_message("ABBCCA", 4)
    assert "AC_CBBA" == message

    message = encrypt_message("AABBCC", -1)
    assert "CCBBAA" == message

    with pytest.raises(TypeError):
        encrypt_message("AABBCC", '4')

    with pytest.raises(TypeError):
        encrypt_message(59, 2)

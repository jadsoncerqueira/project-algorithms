from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("cursotrybe", 9) == "byrtosruc_e"
    assert encrypt_message("cursotrybe", 6) == "ebyr_tosruc"
    assert encrypt_message("cursotrybe", 20) == "ebyrtosruc"

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(9999, 9)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("teste", "3")

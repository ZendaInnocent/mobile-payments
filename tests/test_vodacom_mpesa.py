from unittest.mock import patch

from mobile_payments.constants import *
from mobile_payments.vodacom import MPESA


def test_get_encrypted_api_key():
    m_pesa = MPESA(api_key=MPESA_API_KEY, public_key=MPESA_PUBLIC_KEY)

    enc_key = m_pesa.get_encrypted_api_key()

    assert enc_key is not None


@patch('mobile_payments.vodacom.MPESA.get_session_id')
def test_get_session_id(mock_get_session_id):
    mock_get_session_id.return_value = 'some random key'

    m_pesa = MPESA(api_key=MPESA_API_KEY, public_key=MPESA_PUBLIC_KEY)

    session_id = m_pesa.get_session_id()

    assert session_id == 'some random key'

from gopay import Payments
import logging


class TestPayments:
    def test_create_payment(self, payments: Payments, base_payment: dict):
        response = payments.create_payment(base_payment)
        response_body = response.json
        logging.info(f"API Response: {response_body}")

        assert "errors" not in response_body
        assert "id" in response_body
        assert response_body["state"] == "CREATED"

    def test_refund_payment(self, payments: Payments):
        payment_id = 3049525986

        response = payments.refund_payment(payment_id, 1900)
        response_body = response.json
        logging.info(f"API Response: {response_body}")

        assert "errors" in response_body
        error_dict = response_body["errors"][0]
        assert error_dict["error_name"] == "PAYMENT_REFUND_NOT_SUPPORTED"

    def test_payment_status(self, payments: Payments):
        payment_id = 3049525986

        response = payments.get_status(payment_id)
        response_body = response.json
        logging.info(f"API Response: {response_body}")

        assert "errors" not in response_body
        assert response_body["id"] == payment_id
        assert response_body["state"] == "REFUNDED"
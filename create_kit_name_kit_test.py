import sender_stand_request
import data

def get_kit_body(name):
    kit = data.kit_body.copy()
    kit["name"] = name
    return kit

def positive_assert(name):
    auth_token = sender_stand_request.get_new_user_token()
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == name

def negative_assert_code_400(name):
    auth_token = sender_stand_request.get_new_user_token()
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

# ---------- TESTS POSITIVOS ----------
def test_kit_name_1_char():
    positive_assert("a")

def test_kit_name_511_chars():
    positive_assert (
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    )


def test_kit_name_special_chars():
    positive_assert("№%@,")

def test_kit_name_with_spaces():
    positive_assert(" A Aaa ")

def test_kit_name_with_numbers():
    positive_assert("123")

# ---------- TESTS NEGATIVOS ----------
def test_kit_name_empty():
    negative_assert_code_400("")

def test_kit_name_512_chars():
    negative_assert_code_400 (
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    )

def test_kit_name_missing():
    auth_token = sender_stand_request.get_new_user_token()
    kit_body = {}  # Falta el campo name
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_kit_name_wrong_type_number():
    auth_token = sender_stand_request.get_new_user_token()
    kit_body = {"name": 123}
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

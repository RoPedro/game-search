from integrations.is_there_any_deal import isThereAnyDeal_config, itad_mock


def test_itad_should_not_be_enabled_with_empty_token():
    itad_enabled = isThereAnyDeal_config(ITAD_TOKEN=None)

    assert itad_enabled == False


def test_itad_mock_should_return_none_if_token_is_empty():
    should_be_none = itad_mock(42, None)

    assert should_be_none == None

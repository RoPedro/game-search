from integrations.isThereAnyDeal import isThereAnyDeal_config

def test_itad_should_not_be_enabled_with_empty_token():
    itad_enabled = isThereAnyDeal_config(ITAD_TOKEN=None)
    
    assert itad_enabled == False   
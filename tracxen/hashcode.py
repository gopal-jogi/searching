import hashlib

# Expanded list of potential inputs to test
potential_inputs = [
    'groww',
    'Groww',
    'GROWW',
    'groww.com',
    'planttagg',
    'PlantTagg',
    'PLANTTAGG',
    'planttagg.com',
    'grow',
    'planttag',
    'company_name',
    'unique_identifier',
    'company_id',
    '12345',
    '67890',
    'abcdef',
    'Groww India',
    'PlantTagg Inc',
    'tracxn',
    'tracxn_groww',
    'tracxn_planttagg',
    'user_id_1',
    'user_id_2',
    'product_1',
    'product_2',
    'company_123',
    'entity_456',
    'org_groww',
    'org_planttagg',
    'data1',
    'data2',
    'sample_input',
    'test_value',
    'hash_test',
    'sample123',
    'input_example',
    'unique_key',
    'id_001',
    'id_002',
    'identifier_one',
    'identifier_two',
    'hash_this',
    'secure_data',
    'random_string',
    'trial_input',
    'companyXYZ',
    'organizationABC',
    'india_groww',
    'name_planttagg',
    'groww_company_profile',
    'PlantTagg organization',
    'tracxn data',
    'tracxn_groww_data',
    'tracxn_planttagg_data',
    'groww company profile'
    # Add more potential inputs here
]

decoded_hashes = [
    '5b078933041cabe555bd19207db80e322543afe10b336e5a7464d26d4ad553d3',
    'e52e2c80bd694a49de6f0c0b06712c54af3d89577af8836b667cdd0551008de0'
]

for input_str in potential_inputs:
    # Compute SHA-256 hash of the input string
    hash_object = hashlib.sha256(input_str.encode('utf-8'))
    hash_hex = hash_object.hexdigest()
    
    if hash_hex in decoded_hashes:
        print(f"Match found! Input '{input_str}' corresponds to one of the decoded hashes.")
    # Uncomment the following line to see all hash comparisons
    # else:
    #     print(f"Input '{input_str}' does not match any decoded hashes.")

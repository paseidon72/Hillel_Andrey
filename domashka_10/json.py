import json5

input_data = {
    123456: (
        'name',
        22
    ),
    789654: (
        'name1',
        25
    ),
    321465: (
        'name2',
        30
    ),
    135802: (
        'name',
        32
    ),
    133456: (
        'name',
        38
    ),
}

with open('task_1.json5', 'w') as f:
    json5.dump(input_data, f)

import json

from progressive_json_parser import parse


test_object = {
  "students": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "age": 21,
      "subjects": [
        {
          "name": "Math",
          "score": 88
        },
        {
          "name": "English",
          "score": 92
        },
        {
          "name": "History",
          "score": 81
        }
      ]
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "jane@example.com",
      "age": 19,
      "subjects": [
        {
          "name": "Math",
          "score": 95
        },
        {
          "name": "English",
          "score": 89
        },
        {
          "name": "History",
          "score": 93
        }
      ]
    },
    {
      "id": 3,
      "name": "Robert Johnson",
      "email": "robert@example.com",
      "age": 20,
      "subjects": [
        {
          "name": "Math",
          "score": 90
        },
        {
          "name": "English",
          "score": 85
        },
        {
          "name": "History",
          "score": 78
        }
      ]
    }
  ]
}

test_object_str = json.dumps(test_object)
assert parse(test_object_str) == test_object

for i in range(len(test_object_str)):
    try:
        parse(test_object_str[:i])
    except Exception as e:
        assert False, f"Failed at {i}: {e}"

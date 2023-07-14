# Progressive JSON Parser

This is a **progressive** JSON parser written in Python.

Unlike other JSON parsers, it oppurtunistically parses the JSON, even if it is incomplete.
It does this by completing the JSON by closing all the open contexts (`]`, `}`, `"`), adding `null` values for all the missing values, and completing literals (`true`, `false`, `null`).

## Examples

- `[{"example_key": "example_value"}, {}` --> `[{"example_key": "example_value"}, {}]`
- `[{"example_key": "example_value"}]` --> `[{"example_key": "example_value"}]`
- `[{"example_key": "example_value"` --> `[{"example_key": "example_value"}]`
- `[{"example_key": "example_val` --> `[{"example_key": "example_val"}]`
- `[{"example": "` --> `[{"example": ""}]`
- `[{"example":` --> `[{"example": null}]`
- `[{"example` --> `[{"example": null}]`
- `[{"` --> `[{"": null}]`
- `[{` --> `[{}]`
- `[` --> `[]`
- ` ` --> `null`
- `tru` --> `true`
- `fa` --> `false`
- `n` --> `null`

from ast import literal_eval

from lark import Lark, Transformer, Token, UnexpectedToken

"""
TODO:
- Properly handle escaped strings
- Don't actually reverse dicts
"""

json_grammar = r"""
    ?start: value

    ?value: object
          | array
          | string
          | SIGNED_NUMBER    -> number
          | "true"           -> true
          | /t(r(u)?)?$/     -> true
          | "false"          -> false
          | /f(a(l(s)?)?)?$/ -> false
          | "null"           -> null
          | /n(u(l)?)?$/     -> null

    array  : "[" [value ("," value)*] "]"
    object : "{" [pair ("," pair)*] "}"
    pair   : string ":" value

    string : "\"" [/[^"]+/] "\""

    %import common.SIGNED_NUMBER
    %import common.WS

    %ignore WS
"""


class TreeToJson(Transformer):
    array = list
    pair = tuple
    object = lambda self, values: dict(reversed(dict(values[::-1]).items()))
    string = lambda self, values: values[0].value if values else ''
    number = lambda self, values: literal_eval(values[0].value)

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


json_parser = Lark(json_grammar,
                   parser='lalr',
                   lexer='contextual',
                   propagate_positions=False,
                   maybe_placeholders=False,
                   transformer=TreeToJson())

def parse(json_data):
    interactive_parser = json_parser.parse_interactive(json_data)

    while True:
        try:
            interactive_parser.resume_parse()
        except UnexpectedToken as e:
            if not e.token.type == '$END':
                raise e
            completion_tokens = ['RBRACE', 'RSQB', 'NULL', 'DBLQUOTE', 'COLON']
            accepts = e.interactive_parser.accepts()
            for completion_token in completion_tokens:
                if completion_token in accepts:
                    interactive_parser.feed_token(Token(completion_token, ''))
                    break
            else:
                raise e
            continue
        else:
            break

    result = interactive_parser.parser_state.value_stack.pop()
    return result

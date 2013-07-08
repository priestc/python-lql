from pyparsing import Word, alphanums, oneOf, Group, QuotedString, delimitedList

ALL_OPERATORS = [
    'after',
    'exact',
    '=',
    '==',
    'matches',
    'lessthan',
    'greaterthan',
    'after',
    'before',
    'is_present'
]

class Query(object):
    def __init__(self, as_string=None, ast=None):
        self.ast = ast
        self.as_string = as_string

        if not ast and not as_string:
            raise ValueError("Must include either ast or as_string")
        elif not as_string:
            self.as_string = self._calc_string(ast)
        elif not ast:
            self.ast = self._calc_ast(as_string)

    def _calc_string(self, ast):
        """
        Convert a list structure of LQL and convert it into a string.
        """
        clauses = []
        for clause in ast:
            ## each clause ('including, [double list])
            polarity = clause[0]
            subclauses = clause[1]
            rendered_subclauses = []

            for sc in subclauses:
                if ' ' in sc[2]:
                    # there is a space character in the 'value' space,
                    # wrap in quotation marks
                    sc[2] = '"%s"' % sc[2]
                rendered = ' '.join(sc)
                rendered_subclauses.append(rendered)

            str_subclauses = ','.join(rendered_subclauses)
            clause_str = polarity + ' ' + str_subclauses
            clauses.append(clause_str);

        return ';'.join(clauses)

    def _calc_ast(self, as_string):
        """
        Turn a string LQL query into a "list of lists" object for easier handling.
        """
        identifier = Word("/_.*"+alphanums)
        polarity = oneOf("including excluding", caseless=True)
        operator = oneOf(" ".join(ALL_OPERATORS), caseless=True)
        value = QuotedString("'") | QuotedString('"') | identifier
        key = identifier

        subclause = Group(key + operator + value)
        clause = Group(polarity + Group(delimitedList(subclause, delim=',')))

        lql = delimitedList(clause, delim=';')
        parsed_obj = lql.parseString(as_string)

        parsed_native = eval(str(parsed_obj))

        return parsed_native
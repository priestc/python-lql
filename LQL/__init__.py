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
    def __init__(self, as_string=None, as_list=None):
        self.as_list = as_list
        self.as_string = as_string

        if not as_list and not as_string:
            raise ValueError("Must include either as_list or as_string")
        elif not as_string:
            self.as_string = self._calc_string(as_list)
        elif not as_list:
            self.as_list = self._calc_list(as_string)

    def _calc_string(self, as_list):
        """
        Convert a list structure of LQL and convert it into a string.
        """
        clauses = []
        for clause in as_list:
            ## each clause ('including, [double list])
            polarity = clause[0]
            subclauses = clause[1]
            rendered_subclauses = []

            for sc in subclauses:
                if ' ' in sc[2]:
                    # therre is a space character in the 'value' space, add quote marks
                    sc[2] = '"%s"' % sc[2]
                rendered = ' '.join(sc)
                rendered_subclauses.append(rendered)

            str_subclauses = ','.join(rendered_subclauses)
            clause_str = polarity + ' ' + str_subclauses
            clauses.append(clause_str);

        return ';'.join(clauses)

    def _calc_list(self, as_string):
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
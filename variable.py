class Variable:
    vrs = {}

    def __init__(self, variable_name, variable_value):
        if variable_value in Variable.vrs:
            self._value = Variable.vrs[variable_value]
        else:
            self._value = variable_value
        self._name = variable_name
        Variable.vrs[self._name] = self._value

    def __str__(self):
        return f"Variable name: {self._name}\n" \
               f"Variable value: {self._value}"
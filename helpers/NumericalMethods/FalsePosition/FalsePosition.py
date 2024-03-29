from beautifultable import *
import warnings
from helpers.NumericalMethods.Methods_formulas import MethodsFormulas

warnings.simplefilter(action='ignore', category=FutureWarning)
table = BeautifulTable()


class FalsePosition(MethodsFormulas):

    def __init__(self):
        super().__init__()
        self.iterations = []

    def execute(self, xa: float, xb: float, equation: str, error: float):
        if self.check_sqrt(xa, xb, equation):
            if self.validate_formula(equation):
                table.column_headers = ["it", "xa", "xb", "xr", "F(xa)", "F(xr)", "F(xa)*F(xr)"]
                self.iterations = []
                return self.__process(xa, xb, equation, error)
            else:
                return "La formula no es correcta"
        else:
            return "No hay una raíz en el rango especificado"

    def __process(self, xa: float, xb: float, equation: str, error_range: float, xrold: float = 0, it: int = 0):

        Fxa: float = self.evaluate_formula(equation, xa)
        Fxb: float = self.evaluate_formula(equation, xb)
        xr: float = xb - ((Fxb * (xa - xb)) / (Fxa - Fxb))
        Fxr: float = self.evaluate_formula(equation, xr)
        FxaXFxr = Fxa * Fxr
        table.append_row([it + 1, xa, xb, xr, Fxa, Fxr, FxaXFxr])
        self.iterations.append({"it": it + 1, "xa": xa, "xb": xb, "xr": xr, "fxa": Fxa, "fxr": Fxr, "fxaFxr": FxaXFxr})
        # Caso base
        if (abs(xr - xrold) <= error_range) & it != 0:
            print(table)
            return {"iterations": self.iterations, "result": xr}
        elif FxaXFxr < 0:
            return self.__process(xa, xr, equation, error_range, xr, it + 1)
        else:
            return self.__process(xr, xb, equation, error_range, xr, it + 1)

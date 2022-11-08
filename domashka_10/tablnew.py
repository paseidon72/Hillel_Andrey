import jpype
import asposecells

jpype.startJVM()
from asposecells.api import Workbook

workbook = Workbook("input.csv")
workbook.Save("Output.xlsx")
jpype.shutdownJVM()

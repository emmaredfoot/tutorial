from cyclus.agents import Facility
import cyclus.typesystem as ts

class Storage(Facility):
    """My storage facility."""

    storage_time = ts.Int(
        doc="Minimum amount of time material must be stored",
        tooltip="Minimum amount of time material must be stored",
        units="months",
        uilabel="Storage Time",
        )
    incommod = ts.String(
        tooltip="Storage input commodity",
        doc="Input commodity on which Storage requests material.",
        uilabel="Input Commodity",
        uitype="incommodity",
        )
    outcommod = ts.Int(
        tooltip="Storage output commodity",
        doc="Output commodity on which Storage offers material.",
        uilabel="Output Commodity",
        uitype="outcommodity",
        )
    
    def tick(self):
        print("Hello,")
        print("World!")

from cyclus.agents import Facility
import cyclus.typesystem as ts

class Storage(Facility):
    """My storage facility."""

    # this declares throughput to be of type double for purposes of storage
    # and user input
    throughput = ts.Double(
        doc="Maximum amount of material that can be transferred in or "
            "out each time step",
        tooltip="Maximum amount of material that can be transferred in "
                "or out each time step",
        units="kg",
        uilabel="Maximum Throughput",
        )

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

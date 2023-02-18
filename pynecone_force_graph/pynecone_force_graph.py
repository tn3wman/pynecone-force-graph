# type: ignore
"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
from typing import Set

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

my_data = {
    "nodes": [ 
        { 
          "id": "id1",
          "name": "name1",
          "val": 1 
        },
        { 
          "id": "id2",
          "name": "name2",
          "val": 10 
        }
    ],
    "links": [
        {
            "source": "id1",
            "target": "id2"
        }
    ]
}


class ReactForceGraph(pc.Component):
    tag = "ForceGraph2D"

    graphData: pc.Var[dict]
    width: pc.Var[int] = 1000
    height: pc.Var[int] = 600
    backgroundColor: pc.Var[str] = "lightgray"

    node: pc.Var[dict]

    @classmethod
    def get_controlled_triggers(cls) -> dict[str, pc.Var]:
        return {"on_node_hover": pc.EVENT_ARG}

    @classmethod
    def _get_custom_code(self) -> str:
        return """import dynamic from 'next/dynamic'
const ForceGraph2D = dynamic(() => import('react-force-graph-2d'), { ssr: false });
"""

forcegraph = ReactForceGraph.create


class State(pc.State):

    def set_node(self, _node):
        print("node", _node)


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Eh, kind of works", font_size="2em"),
            pc.box(
                forcegraph(
                    graphData=my_data,
                    width=1000,
                    height=600,
                    backgroundColor="green"),
                ),
            pc.heading("Freezes with on_node_hover", font_size="2em"),
            pc.box(
                forcegraph(
                    graphData=my_data,
                    width=1000,
                    height=600,
                    backgroundColor="red",
                    on_node_hover = lambda node: State.set_node(node)
                    ),
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()

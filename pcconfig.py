import pynecone as pc

config = pc.Config(
    app_name="pynecone_force_graph",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    frontend_packages=[
        'react-force-graph-2d',
    ],
)

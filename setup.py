from setuptools import setup, find_packages

setup(
    name="mcp-simple-openai-assistant",
    version="0.1.0",
    description="A simple MCP server for interacting with OpenAI assistants",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "mcp",
        "openai>=1.0.0"
    ],
    entry_points={
        "console_scripts": [
            "mcp-simple-openai-assistant=mcp_simple_openai_assistant:main",
        ]
    },
)
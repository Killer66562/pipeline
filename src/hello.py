from kfp import dsl, compiler


@dsl.component
def say_hello(name: str) -> str:
    hello_text = f'Hello, {name}!'
    return hello_text


@dsl.pipeline
def hello_pipeline(recipient: str) -> str:
    hello_task = say_hello(name=recipient)
    return hello_task.output

compiler.Compiler().compile(hello_pipeline, 'hello_pipeline.yaml')
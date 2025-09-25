from environs import Env
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

env = Env()
env.read_env()

bind = ":8000"

workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

errorlog = "-"
loglevel = "info"
accesslog = "-"


def post_fork(server, worker):  # type: ignore
    """Post-fork hook to initialize OpenTelemetry tracing in each worker."""
    server.log.info("Worker spawned (pid: %s)", worker.pid)

    resource = Resource.create(attributes={"service.name": env.str("OTEL_SERVICE_NAME")})

    trace.set_tracer_provider(TracerProvider(resource=resource))
    span_processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=env.str("OTEL_EXPORTER_OTLP_ENDPOINT")))
    trace.get_tracer_provider().add_span_processor(span_processor)  # type: ignore

import kfp
import kfp.cli
import kfp.client
import kfp.pipeline_spec
import kfp.pipeline_spec.pipeline_spec_pb2
import kfp.registry

# the namespace in which you deployed Kubeflow Pipelines
namespace = "kubeflow-user-example-com"
path = "/var/run/secrets/kubernetes.io/serviceaccount/token"

# the KF_PIPELINES_SA_TOKEN_PATH environment variable is used when no `path` is set
# the default KF_PIPELINES_SA_TOKEN_PATH is /var/run/secrets/kubeflow/pipelines/token
credentials = kfp.client.ServiceAccountTokenVolumeCredentials(path=path)

client = kfp.Client(host=f"http://ml-pipeline-ui.{namespace}", credentials=credentials)

print(client.list_experiments())
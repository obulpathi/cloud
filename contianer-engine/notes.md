What is a container cluster?

A Container Engine cluster is a group of Compute Engine instances running Kubernetes. It consists of one or more node instances, and a managed Kubernetes master endpoint. A container cluster is the foundation of a Container Engine application—pods, services, and replication controllers all run on top of a cluster.

The Kubernetes master

Every container cluster has a single master endpoint, which is managed by Container Engine. The master provides a unified view into the cluster and, through its publicly-accessible endpoint, is the doorway for interacting with the cluster.

The managed master also runs the Kubernetes API server, which services REST requests, schedules pod creation and deletion on worker nodes, and synchronizes pod information (such as open ports and location) with service information.

Container Engine also upgrades the master to future Kubernetes versions, and integrates with other Google Cloud Services.

Nodes

A container cluster can have one or more node instances. These are managed from the master, and run the services necessary to support Docker containers. Each node runs the Docker runtime and hosts a Kubelet agent, which manages the Docker containers scheduled on the host. Each node also runs a simple network proxy.


What is a pod?

A pod models an application-specific "logical host" in a containerized environment. It may contain one or more containers which are relatively tightly coupled—in a pre-container world, they would have executed on the same physical or virtual host.

Like running containers, pods are considered to be relatively ephemeral rather than durable entities. Pods are scheduled to nodes and remain there until termination (according to restart policy) or deletion. When a node dies, the pods scheduled to that node are deleted. Specific pods are never rescheduled to new nodes; instead, they must be replaced.

What is a replication controller?

A replication controller ensures that a specified number of pod "replicas" are running at any one time. If there are too many, the replication controller kills some pods. If there are too few, it starts more. As opposed to just creating singleton pods or even creating pods in bulk, a replication controller replaces pods that are deleted or terminated for any reason, such as in the case of node failure. For this reason, we recommend that you use a replication controller even if your application requires only a single pod.

What is a service?

Container Engine pods are ephemeral. They can come and go over time, especially when driven by things like replication controllers. While each pod gets its own IP address, those IP addresses cannot be relied upon to be stable over time. This leads to a problem: if some set of pods (let's call them backends) provides functionality to other pods (let's call them frontends) inside a cluster, how do those frontends find the backends?

Enter services.

A service is an abstraction which defines a logical set of pods and a policy by which to access them. The goal of services is to provide a bridge for non-Kubernetes-native applications to access backends without the need to write code that is specific to Kubernetes. A service offers clients an IP and port pair which, when accessed, redirects to the appropriate backends. The set of pods targeted is determined by a label selector.

As an example, consider an image-process backend which is running with 3 live replicas. Those replicas are fungible—frontends do not care which backend they use. While the actual pods that comprise the set may change, the frontend client(s) do not need to know that. The service abstraction enables this decoupling.

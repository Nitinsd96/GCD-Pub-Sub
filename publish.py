from google.cloud import pubsub_v1

# TODO(developer)
project_id = "summer-2020-cmpe-256"
topic_id = "nitin-sunda"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)


ips=["192.168.0.1","192.168.0.2","192.168.0.3","192.168.0.4","192.168.0.5","192.168.0.6","192.168.0.7","192.168.0.8"]


for data in ips:
    # data = f"sss{n}"
    # Data must be a bytestring
    data = data.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)    
    print(future.result())

print("Published messages.")
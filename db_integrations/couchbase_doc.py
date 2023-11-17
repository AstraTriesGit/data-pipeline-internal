from os import environ
from datetime import timedelta
import traceback
from couchbase.exceptions import CouchbaseException
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from dotenv import load_dotenv

load_dotenv()
endpoint = environ.get("CONNECTION_STRING")
username = environ.get("USERNAME")
password = environ.get("PASSWORD")
bucket_name = environ.get("BUCKET_NAME")
scope_name = "_default"
collection_name = "_default"
# Sample airline document
sample_airline = {
    "type": "airline",
    "id": 8091,
    "callsign": "CBS",
    "iata": None,
    "icao": None,
    "name": "Couchbase Airways",
}
# Key will equal: "airline_8091"
key = "airline_8091"

auth = PasswordAuthenticator(username, password)
options = ClusterOptions(auth)
options.apply_profile("wan_development")
try:
    cluster = Cluster(endpoint, options)
    cluster.wait_until_ready(timedelta(seconds=5))
    cb = cluster.bucket(bucket_name)
    cb_coll = cb.scope(scope_name).collection(collection_name)
    try:
        result = cb_coll.insert(key, sample_airline)
        print("\nCreate document success. CAS: ", result.cas)
    except CouchbaseException as e:
        print(e)
    # Simple K-V operation - to retrieve a document by ID
    try:
        result = cb_coll.get(key)
        print("\nFetch document success. Result: ", result.content_as[dict])
    except CouchbaseException as e:
        print(e)
    # Simple K-V operation - to update a document by ID
    try:
        sample_airline["name"] = "Couchbase Airways!!"
        result = cb_coll.replace(key, sample_airline)
        print("\nUpdate document success. CAS: ", result.cas)
    except CouchbaseException as e:
        print(e)
    # Simple K-V operation - to delete a document by ID
    try:
        result = cb_coll.remove(key)
        print("\nDelete document success. CAS: ", result.cas)
    except CouchbaseException as e:
        print(e)
except Exception as e:
    traceback.print_exc()

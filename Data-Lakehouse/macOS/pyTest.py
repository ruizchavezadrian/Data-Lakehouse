from minio import Minio
from minio.error import S3Error

def main():
	client = Minio("127.0.0.1:9000", secure=False, access_key="loPc9XwzYQmtjAy8qW9O", secret_key="aYPx94r1d4GJARuwkkLZXa7Y4MpUjQWIo6rXx4OA")
	buckets = client.list_buckets()
	#for bucket in buckets:
		#print(bucket.name, bucket.creation_date)

# --------------- check bucket

#	bucket_name = "testb"
#	found = client.bucket_exists(bucket_name)
#	print(found)


	# ---------------- make bucket
#	client.make_bucket("bucket1")

	# ------------------ upload file to bucket
	# The file to upload, change this path if needed
	source_file = "./data/iris.parq"

	# The destination bucket and filename on the MinIO server
	bucket_name = "bucket1"
	destination_file = "iris.parq"

	# Make the bucket if it doesn't exist.
	found = client.bucket_exists(bucket_name)
	if not found:
		client.make_bucket(bucket_name)
		print("Created bucket", bucket_name)
	else:
		print("Bucket", bucket_name, "already exists")

	# Upload the file, renaming it in the process
	client.fput_object(
		bucket_name, destination_file, source_file,
	)
	print(
		source_file, "successfully uploaded as object",
		destination_file, "to bucket", bucket_name,
	)
if __name__ == "__main__":
	try:
		main()
	except S3Error as exc:
		print("error occurred.", exc)
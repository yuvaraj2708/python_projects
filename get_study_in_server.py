import requests

def delete_study_by_instance_id(instance_id):
    base_url = "url"
    delete_url = f"{base_url}/{instance_id}"

    try:
        response = requests.delete(delete_url)

        if response.status_code == 200:
            print("Study deleted successfully")
            return True
        else:
            print(f"Failed to delete study. Delete request status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")

    return False

# Usage example
study_instance_id_to_delete = "1.2.840.113745.101000.1008000.38048.4626.5933732"  # Replace with the actual study instance ID
delete_study_by_instance_id(study_instance_id_to_delete)

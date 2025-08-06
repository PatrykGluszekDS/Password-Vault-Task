from password_manager import PasswordManager

def run_mock_tests():
    pm = PasswordManager()
    try:
        # Add mock data
        pm.add_credential("example.com", "admin", "password123", "test account")
        pm.add_credential("another.com", "user", "1234", "")
        
        # Fetch all entries
        records = pm.get_credentials()
        assert len(records) >= 2
        print("Mock records retrieved:", records)

        # Update a record
        pm.update_credential(records[0]['id'], "example.com", "admin", "newpassword", "updated")
        
        # Delete a record
        pm.delete_credential(records[1]['id'])

        # Export test
        pm.export_backup("test_backup.txt")
        print("Backup test complete.")

    except Exception as e:
        print("Test error:", e)
    finally:
        pm.close()

if __name__ == "__main__":
    run_mock_tests()

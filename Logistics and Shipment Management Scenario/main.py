"""
main.py

This file runs test cases against the ShipmentLinkedList class.
Make sure to fill in the methods in 'shipment_linked_list.py' first!
"""

from shipment_linked_list import ShipmentLinkedList

def run_tests():
    # Create a new ShipmentLinkedList
    shipments = ShipmentLinkedList()

    # TEST 1: Insert at Start
    # Insert some shipments at the start to see if the order is reversed.
    shipments.insert_at_start(101)  # This should become head
    shipments.insert_at_start(102)  # This should become new head
    shipments.insert_at_start(103)  # This should become new head
    # Expected list order: 103 -> 102 -> 101
    print("After insert_at_start operations:")
    shipments.print_list()

    # TEST 2: Insert at End
    # Insert shipments at the end.
    shipments.insert_at_end(104)
    shipments.insert_at_end(105)
    # Expected list order now: 103 -> 102 -> 101 -> 104 -> 105
    print("\nAfter insert_at_end operations:")
    shipments.print_list()

    # TEST 3: Insert at Position
    # Insert shipment 999 at position 2 (0-based indexing).
    # Expected list order: 103 -> 102 -> [999] -> 101 -> 104 -> 105
    shipments.insert_at_position(999, 2)
    print("\nAfter insert_at_position (shipment=999, position=2):")
    shipments.print_list()

    # Insert at position 0 (this should behave like insert_at_start).
    shipments.insert_at_position(888, 0)
    # Expected: 888 -> 103 -> 102 -> 999 -> 101 -> 104 -> 105
    print("\nAfter insert_at_position (shipment=888, position=0):")
    shipments.print_list()

    # Insert at a large position (beyond current length).
    # This should behave like insert_at_end.
    shipments.insert_at_position(777, 999)
    # Expected: 888 -> 103 -> 102 -> 999 -> 101 -> 104 -> 105 -> 777
    print("\nAfter insert_at_position (shipment=777, position=999):")
    shipments.print_list()

    # TEST 4: Delete by ID
    # Delete the first occurrence of 999
    result_delete_999 = shipments.delete_by_id(999)
    print("\nDelete shipment 999:", "Success" if result_delete_999 else "Fail")
    # Expected: 888 -> 103 -> 102 -> 101 -> 104 -> 105 -> 777
    shipments.print_list()

    # Try deleting an ID that doesn’t exist (e.g., 555)
    result_delete_555 = shipments.delete_by_id(555)
    print("\nDelete shipment 555:", "Success" if result_delete_555 else "Fail")
    # Expected: No change to list
    shipments.print_list()

    # Delete the head (888)
    shipments.delete_by_id(888)
    # Expected: 103 -> 102 -> 101 -> 104 -> 105 -> 777
    print("\nAfter deleting head (888):")
    shipments.print_list()

    # TEST 5: Search by ID
    # Search for an existing ID
    found_node = shipments.search_by_id(104)
    print("\nSearch for 104. Found:", found_node.shipment_id if found_node else "Not Found")

    # Search for a non-existing ID
    not_found_node = shipments.search_by_id(1111)
    print("Search for 1111. Found:", not_found_node.shipment_id if not_found_node else "Not Found")


if __name__ == "__main__":
    print("Running ShipmentLinkedList Tests...\n")
    run_tests()
    print("\nTests completed.")
